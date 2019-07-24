sudo apt update
sudo apt upgrade
sudo apt install git ffmpeg python3.5 python3-pip
python3.5 -m pip install --upgrade pip
python3.5 -m pip install --upgrade -r requirements.txt

echo install finished
echo now you can run "python3.5 app.py"
echo or to run with ssl, "python app_ssl.py"