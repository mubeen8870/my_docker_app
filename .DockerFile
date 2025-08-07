# Use official Python 3.11 image
FROM python:3.11.-slim


# Set working directory
WORKDIR /app

# Copy requirements.txt first for catching
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Copy All Files and Folders to Container {Working Dir /app}
COPY ..

EXPOSE 5000

CMD [ "python", "app.py" ]   