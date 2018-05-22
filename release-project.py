#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Comandos disponibles:
#
# rp - Actualiza todos los proyectos en local.
# rp {project} - Actualiza el proyecto local especificado.
# rp {project} {environment}  - Actualiza el proyecto en el environment especificado.

import subprocess
import os
import sys
from common import (confirmMessage, printWithColor, getBasePathSource, getNameServer) 
from config_local import (project_names_dev)
from config import (project_names_test, project_names_demo, project_names_prod, enviroment_map_branch, active_projects)

# Obtener el nombre del proyecto.
def getProjectName(project, env = 'dev'):
    if(env == 'dev'):
        return project_names_dev[project]
    elif(env == 'test'):
        return project_names_test[project]
    elif(env == 'demo'):
        return project_names_demo[project]

# Obtener el nombre de la rama.
def getBranchName(env = 'dev'):
    return enviroment_map_branch[env]

# Valida si el proyecto se encuentre dentro de la lista de permitidos.
def validProject(project):
    if not project in active_projects:
        printWithColor('\033[91m The project is not valid.')
        return False
    return True

# Verifica si es un enviroment que se require conectar a un servidor, se le concatena el ssh.
def verifyServer(command_to_run, env="dev"):
    name_server = getNameServer(env)
    if env == 'test' or env == 'demo' or env == 'prod':
        return 'ssh '+ name_server +' "'+ command_to_run +'" ' 
    elif env == 'dev':
        return command_to_run

# Actualiza la solución especificada.
def updateSolution(project, env="dev"):
    os.system('clear')
    print('\n')
    printWithColor('\033[94m ***** Updating project: (' + project + ') in environment ' + env + '*****')
    print('\n')
   
    base_path_source = getBasePathSource(env)
    project_name = getProjectName(project, env)
    branch_name = getBranchName(env)
    directory = base_path_source + project_name
    name_server = getNameServer(env)
    
    base_command = 'cd  ' + directory

    if env=='test' or env=='demo':
        printWithColor('==== Conecting to server {'+ name_server +'}===')
        print('\n')

    # Checkout a rama del enviroment especificado.
    command = verifyServer(base_command +' && git checkout '+ branch_name, env)
    printWithColor('==== Checkout branch ' + branch_name + ' `' + command + '` ===')
    os.system(command)
    print('\n')

    # Hacer pull para bajar cambios.
    command = verifyServer(base_command +' && git pull origin '+ branch_name, env)
    printWithColor('==== Calling pull `'+ command +'` ===')
    os.system(command)
    print('\n')

    # Actualiza composer
    noDev = ''
    if not env == 'dev':
        noDev = '--no-dev'

    command = verifyServer(base_command +' && composer update '+ noDev +' ', env)
    printWithColor('==== Updating composer `'+ command +'` ===')
    os.system(command)
    print('\n')

    # Inicializa la aplicación
    environment = env
    if env == 'dev':
        environment = 'Development'
    command = verifyServer(base_command +' && php init --env='+environment.capitalize()+' --overwrite=All', env)
    printWithColor('==== Init the project `'+command+'` ===')
    os.system(command)
    print('\n')

    # Corre migraciones
    command = verifyServer(base_command +' && php yii migrate --interactive=0', env)
    printWithColor('==== Run migrations  `'+command+'` ===')
    os.system(command)
    print('\n')

    # Aplica metas
    command = verifyServer(base_command +' && php yii metadata', env)
    printWithColor('==== Run metadatas  `'+command+'` ===')
    os.system(command)
    print('\n')

def init():

    numArguments = len(sys.argv)

    # El nombre del archivo lo toma como argumento.
    if numArguments == 1:
        # Si no tiene argumentos se actualizan en local todos los proyectos.
        if(confirmMessage('Are you sure to update all projects in ' + 'environment {development}')):
            for project in active_projects:
                updateSolution(project)

    # Si se le pasa un parametro se toma en cuenta que es un proyecto de local a actualizar.
    elif numArguments == 2:
        project = sys.argv[1]
        if(validProject(project)):
            if(confirmMessage('Are you sure to update {' + project + '} in ' + 'environment {development}')):
                updateSolution(project)

    # Si se le pasa dos parametros se toma en cuenta que el primero es el proyecto y el segundo es el environment.
    elif numArguments == 3:

            project = sys.argv[1]
            env = sys.argv[2]

            if(validProject(project)):
                if(confirmMessage('Are you sure to update {' + project + '} in ' + 'environment {' + env + '}')):
                    updateSolution(project, env)
    else:
        printWithColor('\033[91m Num parameters invalid.')


init()



