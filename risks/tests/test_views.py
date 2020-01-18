import json
from rest_framework import status
from django.test import TestCase
from ..models import Risk, Field, Text, Number, Enum, Date
from profiles.models import User
from ..serializers import RiskSerializer, FieldSerializer
from rest_framework.test import APIClient



# initialize the APIClient app
user = User.objects.get(username='admin')
client = APIClient()
client.force_authenticate(user=user)


class GetAllRisksTest(TestCase):
    """ Test module for GET all Risks API """

    def setUp(self):
        Risk.objects.create(name='Risk 1', description='Risk 1 description')
        Risk.objects.create(name='Risk 2', description='Risk 2 description')

    def test_get_all_risks(self):
        # get API response
        response = client.get('/risks/')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllFieldsTest(TestCase):
    """ Test module for GET all Field API """

    def setUp(self):
        risk = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')
        Text.objects.create(value='Text 1')
        Date.objects.create(value='2017-10-29T16:29:08.175Z')
        Number.objects.create(value=1)
        Enum.objects.create(value='age')
        text1 = Text.objects.get(value='Text 1')
        date1 = Date.objects.get(value='2017-10-29T16:29:08.175Z')
        number1 = Number.objects.get(value=1)
        enum1 = Enum.objects.get(value='age')
        Field.objects.create(name='Field 1', value=text1, risk_id=risk.id)
        Field.objects.create(name='Field 2', value=date1, risk_id=risk.id)
        Field.objects.create(name='Field 3', value=number1, risk_id=risk2.id)
        Field.objects.create(name='Field 4', value=enum1, risk_id=risk2.id)


    def test_get_all_fields(self):
        risk = Risk.objects.get(name='Risk 1')
        # get API response
        response = client.get('/fields/')
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #test that you can only get fields for specific risks
        response = client.get('/fields/risk/'+ str(risk.id) +'/')
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleRiskTest(TestCase):
    """ Test module for GET single Risk API """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')

    def test_get_valid_single_risk(self):
        response = client.get('/risks/'+str(self.risk1.id)+'/')
        self.assertEqual(response.data.get('id'), self.risk1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk(self):
        response = client.get('/risks/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewRiskTest(TestCase):
    """ Test module for inserting a new Risk """

    def setUp(self):
        self.valid_payload = {
            'name': 'Risk 1',
            'description': 'Risk 1 description'
        }

        self.invalid_payload = {
            'names': 'Risk 1',
            'description': 'Risk 1 description'
        }

    def test_create_valid_risk(self):
        response = client.post('/risks/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk(self):
        response = client.post('/risks/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class UpdateSingleRiskTest(TestCase):
    """ Test module for updating an existing risk record """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')

        self.valid_payload = {
            'name': 'Risk updated 1',
            'description': 'Risk updated 1 description'
        }

        self.invalid_payload = {
            'names': 'Risk updated 1',
            'description': 'Risk  updated 1 description'
        }

    def test_valid_update_risk(self):
        response = client.put('/risks/'+ str(self.risk1.id) + '/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_risk(self):
        response = client.put('/risks/'+ str(self.risk1.id) + '/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class GetSingleFieldTest(TestCase):
    """ Test module for GET single Field API """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')
        Date.objects.create(value='2017-10-29T16:29:08.175Z')
        Enum.objects.create(value='age')
        date1 = Date.objects.get(value='2017-10-29T16:29:08.175Z')
        enum1 = Enum.objects.get(value='age')
        self.field1 = Field.objects.create(name='Field 1', value=enum1, risk_id=self.risk1.id)
        self.field2 = Field.objects.create(name='Field 2', value=date1, risk_id=self.risk2.id)

    def test_get_valid_single_field(self):
        response = client.get('/fields/'+ str(self.field1.id) +'/')
        self.assertEqual(response.data.get('id'), self.field1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_field(self):
        response = client.get('/fields/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class CreateNewFieldTest(TestCase):
    """ Test module for inserting a new Field """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.text1 = Text.objects.create(value='Text 1')
        self.number1 = Number.objects.create(value=5)

        self.payload = {
            'name': 'Field 1',
            'value' : 'Text 1',
            'type': 'text',
            'risk_id': self.risk1.id
        }


    def test_create_field(self):
        response = client.post('/fields/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateSingleFieldTest(TestCase):
    """ Test module for updating an existing field record """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')
        self.text1 = Text.objects.create(value='Text 1')
        self.number1 = Number.objects.create(value=5)
        self.field1 = Field.objects.create(name='Field 1', value=self.text1, risk_id=self.risk1.id)
        self.field2 = Field.objects.create(name='Field 2', value=self.number1, risk_id=self.risk2.id)

        self.payload = {
            'name': 'Field updated 1',
            'value': 'age',
            'type': 'enum',
            'risk_id': 13
        }


    def test_update_field(self):
        response = client.put('/fields/'+ str(self.field1.id) + '/',
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSingleRiskTest(TestCase):
    """ Test module for deleting an existing risk record """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')

    def test_valid_delete_risk(self):
        response = client.delete('/risks/'+ str(self.risk1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_risk(self):
        response = client.delete('/risks/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class DeleteSingleFieldTest(TestCase):
    """ Test module for deleting an existing field record """

    def setUp(self):
        self.risk1 = Risk.objects.create(name='Risk 1', description='Risk 1 description')
        self.risk2 = Risk.objects.create(name='Risk 2', description='Risk 2 description')
        self.text1 = Text.objects.create(value='Text 1')
        self.number1 = Number.objects.create(value=5)
        self.field1 = Field.objects.create(name='Field 1', value=self.text1, risk_id=self.risk1.id)
        self.field2 = Field.objects.create(name='Field 2', value=self.number1, risk_id=self.risk2.id)

    def test_valid_delete_field(self):
        response = client.delete('/fields/'+ str(self.field1.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_field(self):
        response = client.delete('/fields/30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
