```python
from django.db import models

class Ship(models.Model):
    name = models.CharField(max_length=255)

class ShipSailingSchedule(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    port_name = models.CharField(max_length=255)
    port_code = models.CharField(max_length=255)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    voyage_type = models.CharField(max_length=255)
    port_type = models.CharField(max_length=255)

class Position(models.Model):
    name = models.CharField(max_length=255)

class PositionAndContractLength(models.Model):
    position_name = models.ForeignKey(Position, on_delete=models.CASCADE)
    contract_length = models.IntegerField()
    onboard_months = models.IntegerField()
    vacation_months = models.IntegerField()

class ShipCrewAllowance(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    allowance_count = models.IntegerField()

class CertificateTypesAndExpiry(models.Model):
    certificate_name = models.CharField(max_length=255)
    expiry_date = models.DateField()
```