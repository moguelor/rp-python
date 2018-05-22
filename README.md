# Release Project (Python)

Update all projects.

1. Install `python3` with `brew` or with installer in the page https://www.python.org/download/releases/3.0/.
2. Create the file `config_local.py`
2. Config your projects names folders depending your local:

```python
project_names_dev = { 
    'contest' : 'contest-backend', 
    'ask' : 'ask-backend', 
    'rewards' : 'social', 
    'coupon' : 'coupon', 
    'mybusiness' : 'core'
}
```

5. Config the base local source, this directory has all your swapwink's proyects.
  
```python
base_path_local_source = '/Users/josemoguel/Documents/fuentes/swapwink/'
```
6. Generate a link to file `release-project.py`.
```
ln -s /Users/josemoguel/Documents/scripts-python/release-project.py rp
```
7. Search your python3 path with `wich python3`
```
/usr/bin/python3
```
8. Move the file `rp` to `/usr/bin/rp` to access the command globally.
```
mv rp /usr/bin/rp
```
9. Run rp

# Commands

1. You can release all projects in the environment `dev`:
```
rpr
```
