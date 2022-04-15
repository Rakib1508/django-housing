# ComfyHomes

A web application for housing market activities built with Python-Django, MongoDB, PostgreSQL, Redis, etc.

## Getting started

Housing is one the fundamental every day necessities for any human being. In this age of technology, marketplaces are becoming more and more customer-oriented to make it easy for them to make decisions. But housing markets are still very complicated and people find it very difficult to choose the right option for themselves from a large number of choices and so many criteria to consider. I am trying to build this web application to simulate a probable online housing market for everyone (buyer, seller, contractor, agencies, developers, etc.) to have a quick and accurate overview of housing entities at ease all in one place.

## Name
ComfyHomes - The Django Housing Web Application

## Description

ComfyHomes is a web application simulating an online housing market with the aim to make it easy for sellers, customers or any other relevant entities to deal with complicated real-world negotiation process at ease online. This app allows users to find housing entities suited to their needs, make detailed investigation, put reviews and feedbacks, find investment opportunities, negotiate and keep track of ongoing and completed transactions, and many more!

[comment]: <> (## Badges)
[comment]: <> (On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.)

[comment]: <> (## Visuals)
[comment]: <> (Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.)

## Installation

To get started with this project, clone this repository to your local machine, install all the necessary modules and dependencies, and that's it! For a guideline, open a directory in your computer, then run the following commands:

```
git clone https://github.com/rifatrakib/comfy-homes.git
cd comfy-homes
pip install -r requirements.txt
```

If you want to have a separate environment for your works, create one before running the `pip` commands and then point your project folder to access the corresponding Python interpreter. Don't forget to activate your package manager before executing `pip` commands.

If you want to follow along the project step by step, please open a directory and follow the commands given below:

```
mkdir comfy-homes
cd comfy-homes
```

If you want to have a separate environment for your works, create one before running the `pip` commands and then point your project folder to access the corresponding Python interpreter. Then activate your package manager and run these commands:

```
pip install django django-dotenv pandas psycopg2 redis boto3 mysqlclient djongo
pip freeze > requirements.txt
django-admin startproject core .
```

Check your database connections using the following commands:

```
python manage.py check --database auth_db
python manage.py check --database app_db
python manage.py check --database dynamic_db
```

Create a `.env` file at the root directory and include these following variables in that file as these are secrets.

- DJANGO_SECRET_KEY (add a complex key that is hard to be guessed, make it a long string having no possible patterns. It's better to generate it via the django.core.management.utils.get_random_secret_key function)
- DEBUG (if 1, then True i.e. run development server; else False)
- DJANGO_ALLOWED_HOST (host name as a string to be used when DEBUG is False)

And all other variables in `settings.py` that are using the `os` module's `os.environ.get()` function to read values from your `.env` file.

Run the following commands in a terminal with your package manager activated to get a secure secret key:

```
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

A list of all variables to be included in the `.env` will be given as the project reaches each checkpoints as it keeps growing. In the meantime, please refer to the `core/settings.py` file to see all the necessary variables that are being read from the `.env` file.

[comment]: <> (## Usage)
[comment]: <> (Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.)

## Support

To get in touch, contact me via:

- [Gmail - abdur.rakib.1508@gmail.com](mailto:abdur.rakib.1508@gmail.com)
- [Outlook - Rakib.1508@outlook.com](mailto:Rakib.1508@outlook.com)
- [LinkedIn - Muhammad Abdur Rakib](https://www.linkedin.com/in/md-abdur-rakib-1508/)
- [Twitter - @Muhammad16052](https://twitter.com/Muhammad16052)
- [FaceBook - Muhammad Abdur Rakib](https://www.facebook.com/rifat.rakib.1508/)
- [Instagram - @rakib_1508](https://www.instagram.com/rakib_1508/)

## Roadmap

This is just a application simulation, so things might not be as sophisticated as a real world app would be. But I still want to continue to develop this app for a while. With that in mind, this is the current plan to achieve step by step:

- [] Build necessary RDS schemas for PostgrsSQL database.
- [] Dynamic role-based authentication system.
- [] Build a scraper to start collecting housing data and set a storage in an Amazon S3 bucket which will be our data lake.
- [] Build a data pipeline to process the housing data from S3 so that they can be used for the application.
- [] Build an end-to-end data pipeline starting from data collection via scraper to storing production-ready processed data in MongoDB and RDS.
- [] Enhance performance by integrating Redis.
- [] Extend data pipeline to update Redis storage anytime there is any data updates.
- [] Transaction gateway integration.
- [] User data collection mechanism to collect valuable user data and store in S3 and relevant databases.
- [] Bring in some machine learning models for recommendations and estimations.
- To be continued!

## Contributing

For people who want to make changes to this project, please make a separate branch with your name followed by `_branch` as the branch name. And for convenience, reach out to me on any of the platforms I shared above for a better collaboration. I am open to ideas from anyone and will consider including it in the roadmap.

This repository is mostly dedicated to building backend APIs and other Python-based works. If anyone is interested to contribute with a frontend part for this app, please reach out to me on a social platform before making any changes on this repository so that we can hash out the necessary upgrades the whole system needs.

This project is not aimed to be used for commercial use at this moment. If anyone wants to use it for their own commercial uses, please send me an email before you do so. Except for collaboration, I am not looking for any financial contributions for this project.

## Authors and acknowledgment

At this moment, I am the only author for this project. In future, if more developers and contributers come along, I will be happy to acknowledge their contributions and share their credentials if necessary.

## License

No licenses included to this project at this moment. But in future, something may come along considering the needs.

## Project status

This project is just starting at this moment. We can call this phase as preheating phase for ComfyHomes.
