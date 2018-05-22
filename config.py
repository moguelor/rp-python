#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

# Nombre del servidor de test.
name_server_test = 'test-swapwink'

# Nombre del servidor de producción.
name_server_prod = 'ec2.swapwink.com'

# Proyectos activos.
active_projects = ['mybusiness', 'coupon', 'contest', 'ask', 'rewards']

# Ambientes válidos.
active_enviroments = ['dev', 'test', 'demo', 'prod']

# Relacion enviroment -> rama
enviroment_map_branch = {'dev':'development', 'test' : 'stable', 'demo' : 'demo', 'prod' : 'master'}

# Relaciones nombre_clave -> proyecto por enviroment
project_names_test = { 'contest' : 'stable-contest', 'ask' : 'stable-ask', 'rewards' : 'stable-rewards', 'coupon' : 'stable-coupon', 'mybusiness' : 'stable-mybusiness'}
project_names_demo = { 'contest' : 'demo-contest', 'ask' : 'demo-ask', 'rewards' : 'demo-rewards', 'coupon' : 'demo-coupon', 'mybusiness' : 'demo-mybusiness'}
project_names_prod = { 'contest' : 'contest', 'ask' : 'ask', 'rewards' : 'rewards', 'coupon' : 'coupon', 'mybusiness' : 'mybusiness'}
