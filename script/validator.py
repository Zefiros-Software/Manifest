from jsonschema import validate
import json
import sys
import os

def checkAssets():
    with open('.assets.json') as assetFile:    
        assets = json.load(assetFile)

    assetsSchema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": {
            "type" : "object",
            "minProperties": 2,
            "maxProperties": 3,
            "properties" : {
                "name": {
                    "type": "string",
                    "pattern": "^([a-zA-Z0-9_-]{2,50}/[a-zA-Z0-9_-]{2,50})$"
                },
                "repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$"
                },
                "shadow-repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$",
                    "optional": True
                }
            }
        }
    }

    validate(assets, assetsSchema)
    assetNames = set()
    for asset in assets:
        print( "Checking %s..." % asset["name"] )
        if asset["name"] in assetNames:
            print( "There is a duplicate '%s' in _assets.json'!" % asset["name"] )
            sys.exit(-1)
        else:
            assetNames.add( asset["name"] )

            #code = os.system( "git ls-remote --exit-code -h %s > null" % asset["repository"])

            #if code != 0:
            #    print( "The repository '%s' for asset '%s' is unaccessible!" % (asset["repository"], asset["name"]) )
            #    sys.exit(-1)

def checkManifest():
    with open('.manifest.json') as manifestFile:    
        manifests = json.load(manifestFile)

    manifestsSchema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": {
            "type" : "object",
            "minProperties": 2,
            "maxProperties": 3,
            "properties" : {
                "name": {
                    "type": "string",
                    "pattern": "^([a-zA-Z0-9_-]{2,50}/[a-zA-Z0-9_-]{2,50})$"
                },
                "repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$"
                },
                "shadow-repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$",
                    "optional": True
                }
            }
        }
    }

    validate(manifests, manifestsSchema)
    manifestNames = set()
    for manifest in manifests:
        print( "Checking %s..." % manifest["name"] )
        if manifest["name"] in manifestNames:
            print( "There is a duplicate '%s' in _manifests.json'!" % manifest["name"] )
            sys.exit(-1)
        else:
            manifestNames.add( manifest["name"] )

            #code = os.system( "git ls-remote -q --exit-code -h %s" % manifest["repository"])

            #if code != 0:
            #    print( "The repository '%s' for manifest '%s' is unaccessible!" % (manifest["repository"], manifest["name"]) )
            #    sys.exit(-1)


def checkModules():
    with open('.modules.json') as modulesFile:    
        moduless = json.load(modulesFile)

    modulessSchema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": {
            "type" : "object",
            "maxProperties": 2,
            "properties" : {
                "name": {
                    "type": "string",
                    "pattern": "^([a-zA-Z0-9_-]{2,50}/[a-zA-Z0-9_-]{2,50})$"
                },
                "repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$"
                }
            }
        }
    }

    validate(moduless, modulessSchema)
    modulesNames = set()
    for modules in moduless:
        print( "Checking %s..." % modules["name"] )
        if modules["name"] in modulesNames:
            print( "There is a duplicate '%s' in _moduless.json'!" % modules["name"] )
            sys.exit(-1)
        else:
            modulesNames.add( modules["name"] )

            #code = os.system( "git ls-remote -q --exit-code -h %s" % modules["repository"])

            #if code != 0:
            #    print( "The repository '%s' for modules '%s' is unaccessible!" % (modules["repository"], modules["name"]) )
            #    sys.exit(-1)


def checkRegistries():
    with open('.registries.json') as registriesFile:    
        registriess = json.load(registriesFile)

    registriessSchema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": {
            "type" : "object",
            "maxProperties": 2,
            "properties" : {
                "name": {
                    "type": "string",
                    "minLength": 2,
                    "maxLength": 50,
                    "pattern": "^([a-zA-Z0-9_-]*)$"
                },
                "repository": {
                    "type": "string",
                    "pattern": "^(https://.*\.git)$"
                }
            }
        }
    }

    validate(registriess, registriessSchema)
    registriesNames = set()
    for registries in registriess:
        print( "Checking %s..." % registries["name"] )
        if registries["name"] in registriesNames:
            print( "There is a duplicate '%s' in _registriess.json'!" % registries["name"] )
            sys.exit(-1)
        else:
            registriesNames.add( registries["name"] )

            #code = os.system( "git ls-remote -q --exit-code -h %s" % registries["repository"])

            #if code != 0:
            #    print( "The repository '%s' for registries '%s' is unaccessible!" % (registries["repository"], registries["name"]) )
            #    sys.exit(-1)

print( "Checking assets..." )
checkAssets()
print( "\nChecking manifest..." )
checkManifest()
print( "\nChecking modules..." )
checkModules()
print( "\nChecking registries..." )
checkRegistries()

print( "All json files validated." )