sudo apt update
sudo apt upgrade
sudo apt install git ffmpeg python3.5 python3-pip -y
python3.5 -m pip install --upgrade pip
python3.5 -m pip install --upgrade -r requirements.txt

echo install finished
echo now you can run "python app.py"
echo or to run with ssl, setup with looking README.md
echo For more informationes visit https://github.com/SDR-Roul/Yuda
