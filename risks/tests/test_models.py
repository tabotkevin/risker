from django.test import TestCase
from ..models import Risk, Field, Text, Number, Enum, Date
from django.db import IntegrityError


class RiskTest(TestCase):
    """ Test module for Risk model """

    def setUp(self):
        Risk.objects.create(name='Risk 1', description='Risk 1 description')
        Risk.objects.create(name='Risk 2', description='Risk 2 description')

    def test_risk_attributes(self):
        risk1 = Risk.objects.get(name='Risk 1')
        risk2 = Risk.objects.get(name='Risk 2')
        self.assertEqual(risk1.name, "Risk 1")
        self.assertEqual(risk1.description, "Risk 1 description")
        self.assertEqual(risk2.name, "Risk 2")
        self.assertEqual(risk2.description, "Risk 2 description")
        self.assertIsNotNone(risk1.id)
        self.assertIsNotNone(risk2.id)


class FieldTest(TestCase):
    """ Test module for Field model """

    def setUp(self):
        Risk.objects.create(name='Riskf 1', description='Riskf 1 description')
        Risk.objects.create(name='Riskf 2', description='Riskf 2 description')
        Text.objects.create(value='Text 1')
        Date.objects.create(value='2017-10-29T16:29:08.175Z')
        Number.objects.create(value=1)
        Enum.objects.create(value='age')
        riskf1 = Risk.objects.get(name='Riskf 1')
        riskf2 = Risk.objects.get(name='Riskf 2')
        text1 = Text.objects.get(value='Text 1')
        date1 = Date.objects.get(value='2017-10-29T16:29:08.175Z')
        number1 = Number.objects.get(value=1)
        enum1 = Enum.objects.get(value='age')
        Field.objects.create(name="Field 1", value=text1, risk_id=riskf1.id)
        Field.objects.create(name='Field 2', value=date1, risk_id=riskf2.id)
        Field.objects.create(name='Field 3', value=number1, risk_id=riskf1.id)
        Field.objects.create(name='Field 4', value=enum1, risk_id=riskf2.id)

    def test_field_attributes(self):
        riskf1 = Risk.objects.get(name='Riskf 1')
        riskf2 = Risk.objects.get(name='Riskf 2')
        field1 = Field.objects.get(name='Field 1')
        field2 = Field.objects.get(name='Field 2')
        field3 = Field.objects.get(name='Field 3')
        field4 = Field.objects.get(name='Field 4')
        text1 = Text.objects.get(value='Text 1')
        date1 = Date.objects.get(value='2017-10-29T16:29:08.175Z')
        number1 = Number.objects.get(value=1)
        enum1 = Enum.objects.get(value='age')
        self.assertEqual(field1.name, "Field 1")
        self.assertEqual(field1.value, text1)
        self.assertEqual(field1.value.value, text1.value)
        self.assertEqual(field2.name, "Field 2")
        self.assertEqual(field2.value, date1)
        self.assertEqual(field2.value.value, date1.value)
        self.assertEqual(field3.name, "Field 3")
        self.assertEqual(field3.value, number1)
        self.assertEqual(field3.value.value, number1.value)
        self.assertEqual(field4.name, "Field 4")
        self.assertEqual(field4.value, enum1)
        self.assertEqual(field4.value.value, enum1.value)
        self.assertIsNotNone(field1.id)
        self.assertIsNotNone(field2.id)
        self.assertIsNotNone(field1.risk_id)
        self.assertIsNotNone(field2.risk_id)
        self.assertEqual(field1.risk_id, riskf1.id)
        self.assertEqual(field2.risk_id, riskf2.id)
        
        
        
