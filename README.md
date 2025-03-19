Script to get your Kinopoisk ratings in a Letterboxd-compatible format

Steps:
1. Install requirements: `virtualenv .venv && source .venv/bin/activate && pip3 install -r requirements.txt`
2. Find your user_id on the Kinopoisk: it can be found on the url of your personal page `https://www.kinopoisk.ru/user/{user_id}/`
3. Launch the script with your user_id as an argumant `python3 kp_to_lb_converter.py 12345678`
4. Your csv is ready! Hopefully. Now you can upload it to https://letterboxd.com/import/ 
