# -*- coding: utf-8 -*
# remove old images and stopped containers

import os

# All images
all_images_ret = os.popen("docker images --no-trunc | grep -v REPOSITORY ")
all_images_list = all_images_ret.readlines()


ret = os.popen("docker ps -a |grep -v CREATED|awk \'{print $2}\'")
used_image_list = ret.readlines()

for item_of_list in all_images_list:
    image_list = item_of_list.replace("\n", "").split()
    image_name = image_list[0] + ":" + image_list[1]
    image_id = image_list[2]

    if str(used_image_list).find(image_name) == int('-1'):
        print(image_name + " is not used")
        exec_shell = "docker rmi " + image_id
        del_ret = os.system(exec_shell)
        print(del_ret)
        if del_ret == 0:
            print(image_name + " has been deleted!")
