FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# This should be set in the .env file which is not pushed to repository. I'll keep
# password here for simplicity.
ENV DJANGO_SECRET_KEY 'y0+2+@-*itbeq8nh*fh0m#=cf1e!77g@9&tl-3v_+y$8gzs%&l'
ENV PSQLPASSWORD 'mystrongpassword'
ENV PSQLHOST 'db'

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt


