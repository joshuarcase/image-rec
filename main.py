import os

# Number of images
photo_count = 0
dir = './input'
for path in os.listdir(dir):
  if os.path.isfile(os.path.join(dir, path)):
    photo_count += 1
print('test dir count: ', photo_count, '\n')

# Fun image code



# Do for every input
while photo_count != 0:
  print('counted one image')
  photo_id()
  photo_count -= 1
else:
  print('\nAll images identified!')

