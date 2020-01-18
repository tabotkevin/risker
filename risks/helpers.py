
from risks.models import Text, Date, Number, Enum

def get_field_value(type, val):
	value = None
	if type == 'text':
		value = Text.objects.create(value=val)
	if type == 'enum':
		value = Enum.objects.create(value=val)
	if type == 'date':
		value = Date.objects.create(value=val)
	if type == 'number':
		value = Enum.objects.create(value=val)
	return value