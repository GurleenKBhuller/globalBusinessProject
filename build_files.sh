echo "BUILD START"
python -m pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "BUILD END"