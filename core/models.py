"""
Core module model definition
"""

import uuid

from django.db import models


class Article(models.Model):
    """
    A representation of an Article
    :field id: (auto pk) Article ID
    :field title: (str) Title of article
    :field content: (str) Content of article
    :field created_at: (datetime) Article creation date
    :field updated_at: (datetime) Article updated date
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100, editable=True, unique=True)
    content = models.TextField(editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Rename table core_article to article
        """
        db_table = "article"
