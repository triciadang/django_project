from django.test import TestCase
from trial_app.forms import CreateBookForm

class TestForms(TestCase):


	def test_valid_data(self):
		form = CreateBookForm(data={
			'title':'Title1',
			'author':'Author1',
			'summary':'summary1',
			'your_email':'email@email.com'
			})

		self.assertTrue(form.is_valid())

	def test_no_title(self):
		form=CreateBookForm(data={
			'title':'',
			'author':'Author1',
			'summary':'summary1',
			'your_email':'email@email.com'
			})
		self.assertFalse(form.is_valid())

	def test_no_author(self):
		form=CreateBookForm(data={
			'title':'Title1',
			'author':'',
			'summary':'summary1',
			'your_email':'email@email.com'
			})

		self.assertFalse(form.is_valid())

	def test_no_summary(self):
		form=CreateBookForm(data={
			'title':'Title1',
			'author':'Author1',
			'summary':'',
			'your_email':'email@email.com'
			})

		self.assertFalse(form.is_valid())

	def test_wrong_email(self):
		form=CreateBookForm(data={
			'title':'',
			'author':'Author1',
			'summary':'summary1',
			'your_email':'emailemail.com'
			})

		self.assertFalse(form.is_valid())

	def test_wrong_email2(self):
		form=CreateBookForm(data={
			'title':'',
			'author':'Author1',
			'summary':'summary1',
			'your_email':'email@'
			})

		self.assertFalse(form.is_valid())