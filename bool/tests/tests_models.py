from django.test import TestCase
from bool.models import User, Post, Profile, Comments
from faker import Faker
import random

faker = Faker("pl_PL")


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User(username='TestUser', password='tester', email='test@tester.com')

    def test_user_add(self):
        self.user.save()
        self.assertIsNotNone(self.user.id)


class PostModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.posts = []
        for i in range(5):
            profile = Profile.objects.create(
                user=User.objects.create_user(
                    username=self.fake.user_name(),
                    password=self.fake.password(),
                    email=self.fake.email()
                ),
            )
            post = Post.objects.create(
                question=self.fake.text(),
                answer=self.fake.text(),
                profile=profile
            )
            self.posts.append(post)

    def test_post_add(self):
        for post in self.posts:
            self.assertIsNotNone(post.id)

    def test_post_add(self):
        random_posts = random.sample(self.posts, 2)

        for post in random_posts:
            self.assertIsNotNone(post.id)
            # print(post.question)
            # print(post.answer)
            # print(post.profile.user.username)


class CommentsModelTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.comments = []
        for i in range(2):
            profile = Profile.objects.create(
                user=User.objects.create_user(
                    username=self.fake.user_name(),
                    password=self.fake.password(),
                    email=self.fake.email()
                ),
            )
            post = Post.objects.create(
                question=self.fake.text(),
                answer=self.fake.text(),
                profile=profile
            )
            comment = Comments.objects.create(
                text=self.fake.text(),
                profile=profile,
            )
            comment.post.add(post)
            self.comments.append(comment)

    def test_comment_add(self):
        for comment in self.comments:
            self.assertIsNotNone(comment.id)

# from bool.models import User, Post, Profile, Comments
# from faker import Faker
# import random
# import pytest
#
# faker = Faker("pl_PL")
#
# @pytest.mark.django_db
# def test_user_add():
#     user = User(username='TestUser', password='tester', email='tests@tester.com')
#     user.save()
#     assert user.id is not None
#
# @pytest.mark.django_db
# def test_post_add():
#     fake = Faker()
#     posts = []
#     for i in range(5):
#         profile = Profile.objects.create(
#             user=User.objects.create_user(
#                 username=fake.user_name(),
#                 password=fake.password(),
#                 email=fake.email()
#             ),
#         )
#         post = Post.objects.create(
#             question=fake.text(),
#             answer=fake.text(),
#             profile=profile
#         )
#         posts.append(post)
#
#     for post in posts:
#         assert post.id is not None
#
#     random_posts = random.sample(posts, 2)
#     for post in random_posts:
#         assert post.id is not None
#
# @pytest.mark.django_db
# def test_comment_add():
#     fake = Faker()
#     comments = []
#     for i in range(2):
#         profile = Profile.objects.create(
#             user=User.objects.create_user(
#                 username=fake.user_name(),
#                 password=fake.password(),
#                 email=fake.email()
#             ),
#         )
#         post = Post.objects.create(
#             question=fake.text(),
#             answer=fake.text(),
#             profile=profile
#         )
#         comment = Comments.objects.create(
#             text=fake.text(),
#             profile=profile,
#         )
#         comment.post.add(post)
#         comments.append(comment)
#
#     for comment in comments:
#         assert comment.id is not None
