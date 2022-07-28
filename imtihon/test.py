from unittest import TestCase

from app1.models import *
from app1.serializers import *

class TestSuv(TestCase):
    def setUp(self) -> None:
        self.suv = Suv.objects.last()

    def test_suv(self):
        ser = SuvSer(data = self.suv)
        assert ser.is_valid()
        self.assertTrue(ser.data["id"] is not None)

class test_albom(TestCase):
    def setUp(self) -> None:
        self.mijoz = Mijoz.objects.last()

    def mijoz_tekshir(self):
        ser = MijozSer(data=self.mijoz)
        assert ser.is_valid()
        self.assertTrue(ser.data["id"] is not None)



