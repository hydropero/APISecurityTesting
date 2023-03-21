from flask import Flask, redirect, url_for, request, session, flash, Blueprint
from datetime import timedelta
from SecureFlaskAPI import create_app

app = create_app()


if __name__ == "__main__":
    app.run(port=8011)