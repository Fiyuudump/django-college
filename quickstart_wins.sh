py -m venv myenv

.\myenv\Scripts\activate

cd blog

pip install -r requirement.txt

py manage.py migrate

py manage.py createsuperuser 