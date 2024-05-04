

# Textvault
Text storage and retrieval app using Django REST Framework



##### Setup to run

- Download zip file to your local machine
- Extract the zip file
- Open terminal/cmd promt
- Goto that Path

Example

```
cd ~/Destop/Textvault-master
```


Command line to install all dependencies
```
pip install -r requirements.txt
```

Then
```
cd ../Textvault
```

Command line to run your program
```
python manage.py runserver
```

Now open your browser and go to this address
```
http://127.0.0.1:8000
```


# API Documentation

## 1. Login API
- **Endpoint**: `/login/`
- **Sample Payload**:
  ```json
  {
      "username": "abhinavtp",
      "password": "abhinav123"
  }

-**Note**: `create user with the command 'python manage.py createsuperuser'`

## 2. Refresh API
- **Endpoint**: `/refresh/`
- **Sample Payload**:
  ```json
    {
   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCsdsasfasfafqer4t4t4rtergrgsrgswetgwtgrsrgvsfgdfgdghdfhdfhd"
    }

## 3. Create API
- **Endpoint**: `/create_snippet/`
- **Sample Payload**:
  ```json
    {
   "title": "titlee1",
   "content": "contante1",
   "tag": "tage1"
    }   

## 4. Overview API
- **Endpoint**: `/snippet_detail/<int:snippet_id>/`

## 5. Details API
- **Endpoint**: `/get_all_snippets/`

## 6. Update API
- **Endpoint**: `/update_snippet/<int:snippet_id>/`
- **Sample Payload**:
  ```json
    {
   "title": "title3updated",
   "content": "content3updated",
   "tag": "tag4"
    }

## 7. Delete API
- **Endpoint**: `/delete_snippets/`
- **Sample Payload**:
  ```json
    {
   "ids": [7, 8]
    }

## 8. Taglist API
- **Endpoint**: `/get_all_tags/`

## 9. Taglist API
- **Endpoint**: `/snippets_by_tag_id/<int:tag_id>/`


