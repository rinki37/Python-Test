# # Way 1 to get a secret key -
# import os
# os.urandom(12)

# # Way 2 to get a secret key- 
# import uuid
# uuid.uuid4().hex

# # Way 3 to get a secret key- 
# import secrets
# secrets.token_urlsafe(12)


# In this project, there might occur issues due to package dependencies. 