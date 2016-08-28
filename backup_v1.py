import os
import time

source = ['/home/tomahawk/Desktop/UnicornPoachCustomerDevelopment']
target_dir = '/home/tomahawk/Public/playgrounds/python/backupfiles'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# run the backup
print("Zip command is: ")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print("Successful backup to ", target)
else:
    print("Backup FAILED")
