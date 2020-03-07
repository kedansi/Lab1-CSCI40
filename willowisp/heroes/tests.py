from django.test import TestCase

# Create your tests here.
class HeroesTest(TestCase):
    def test_can_get_create_template(self):
        response = self.client.get('/heroes/')
        self.assertTemplateUsed(response, 'heroes.html')
class CloudTest(TestCase):
    def test_can_get_create_template(self):
        response = self.client.get('/hero/cloud/')
        self.assertTemplateUsed(response, 'detail_cloud.html')
class JesterTest(TestCase):
    def test_can_get_create_template(self):
        response = self.client.get('/hero/jester/')
        self.assertTemplateUsed(response, 'detail_jester.html')
class SunfloweyTest(TestCase):
    def test_can_get_create_template(self):
        response = self.client.get('/hero/sunflowey/')
        self.assertTemplateUsed(response, 'detail_sunflowey.html')
