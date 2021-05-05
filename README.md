# django_audio_file_server

intallation package -- 

  ```
  install python 3.6
  install django 3.2
  install django-rest-framework
  ```

Steps to run the project: 

1. Make Migration
```
	python manage.py makemigrations
```
2. Migrate

```
	python manage.py migrate
```

3. create superuser
```
	python manage.py createsuperuser
  ```

4. runserver
```
	python manage.py runserver
  ```

5. To see django default admin
```
	http://127.0.0.1:8000/admin/
  ```
(Here you can add, delete and update audio by gui)

6. To get all the audiofile detail
```
	http://127.0.0.1:8000/api/audio/
  ```

7. To create an audiofile via rest-api
```
	http://127.0.0.1:8000/api/audio/
  ```

	create a json like:
		{
    			"audioFileType": (Song, Podcast, Audiobook),
    			audioFileMetadata
		}
	For Example:
		{
    			"audioFileType": "Song",
    			"Name": "Attention",
    			"Duration": 120
		}

8. To get the detail of any one audiofile :
	
	for song: 
  
    ```
    http://127.0.0.1:8000/api/detail/Song/<id>
    ```
	
	for podcast:
  
    ```
    http://127.0.0.1:8000/api/detail/Podcast/<id>
    ```

	for audiobook: 
  
    ```
    http://127.0.0.1:8000/api/detail/Audiobook/<id>
    ```

	for example -
	http://127.0.0.1:8000/api/detail/Song/14

similary for update, delete 

```
	http://127.0.0.1:8000/api/detail/<AudioFileType>/<id>
  ```

9. To get all details of any audiotype:

```
	http://127.0.0.1:8000/api/detail/<AudioFileType>
  ```


(Note: http://127.0.0.1:8000 is used for localhost)





	
