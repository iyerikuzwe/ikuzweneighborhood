from django.test import TestCase

# Create your tests here.
from .models import Neighbour, Profile, Business, Posts
from django.contrib.auth.models import User


class HoodTestClass(TestCase):
    """
    Test neighbour class and its functions.
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='ikuzwe', location='kagugu', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbour))

    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.hood.save_hood()
        hoods = Neighbour.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.hood.save_hood()
        self.hood.delete_hood

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.hood.save_hood()
        new_hood = Neighbour.objects.filter(name='ikuzwe').update(name='Bisness')
        hoods = Neighbour.objects.get(name='Bisness')
        self.assertTrue(hoods.name, 'Bisness')

    
    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.hood.save_hood()
        this_hood= self.hood.get_by_id(self.hood.id)
        hood = Neighbour.objects.get(id=self.hood.id)
        self.assertTrue(this_hood, hood)

class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.hood = Neighbour(name='ikuzwe', location='kagugu', user=self.user)
        self.hood.save_hood()
        self.pro = Profile(user=self.user, hood = self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.pro, Profile))


    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.pro.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.pro.save_profile()
        self.pro.del_profile()


class BusinessTestClass(TestCase):
    """
    Test business class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='ikuzwe', location='kagugu', user=self.user)
        self.hood.save_hood()
        self.biz = Business(name="bisness", email="ikuzwe@gmail.com", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.biz, Business))

    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.biz.save_biz()
        bizes = Business.objects.all()
        self.assertTrue(len(bizes) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.biz.save_biz()
        self.biz.delete_biz()

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.biz.save_biz()
        new_biz = Business.objects.filter(name='bisness').update(name='bisnesses')
        bizes = Business.objects.get(name='bisnesses')
        self.assertTrue(bizes.name, 'bisnesses')


    def test_get_by_id(self):
        """
        Function to test if you can get a hood by its id
        """
        self.biz.save_biz()
        this_biz= self.biz.get_by_bizid(self.biz.id)
        biz = Business.objects.get(id=self.biz.id)
        self.assertTrue(this_biz, biz)



class PostsTestClass(TestCase):
    """
    Test posts class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='ikuzwe', location='kagugu', user=self.user)
        self.hood.save_hood()
        self.post = Posts(body="bisness", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    
    def test_save_method(self):
        """
        Function to test that a post is being saved
        """
        self.post.save_posts()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.post.save_posts()
        self.post.del_posts()

    def test_update_method(self):
        """
        Function to test that a post's details can be updated
        """
        self.post.save_posts()
        new_posts = Posts.objects.filter(body='bisness').update(body='bisnesses')
        bizes = Posts.objects.get(body='bisnesses')
        self.assertTrue(bizes.body, 'bisnesses')

        
 















