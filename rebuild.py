import os, sys
from shutil import which

print("Kill running portolio containers")
os.system("docker kill portfolio")

print("build from new context...")
os.system("docker build -t portfolio:v1 .")

print("run new container...")
os.system("docker run --name portfolio -d -p 80:80 portfolio:v1")
