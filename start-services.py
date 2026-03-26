#!/usr/bin/env python3
import subprocess

homepage = "apps/homepage/homepage.yaml"
database = "database/postgres-pgadmin.yaml"

database_command = "docker-compose -f " + database + " up -d"
homepage_command = "docker-compose -f " + homepage + " up -d"

result = subprocess.run(database_command, shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print(result.stderr)
    print(result.stdout)
else:
    print("Add some kind of error here!")
    
result = subprocess.run(homepage_command, shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print(result.stderr)
    print(result.stdout)
else:
    print("Add some kind of error here!")