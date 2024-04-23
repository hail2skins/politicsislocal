from django.db import models

# Create your models here.

'''
Donors model

The Donor model will have required fields last_name, first_name, street_number, street_name,
city, state, zip_code, and needs_review. The needs_review field will be a boolean field that
defaults to False.

This model will relate heavily to the Contributions model below. 

'''
class Donor(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255, null=True)  # Allow NULL values
    street_name = models.TextField(null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=5, null=True)
    needs_review = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_address(self):
        return f"{self.street_number} {self.street_name}, {self.city}, {self.state} {self.zip_code}"
    
'''
Contributions model

The Contributions model will have required fields donor, date, and amount. The donor field will
be a foreign key to the Donor model. The date field will be a DateField and the amount field will
be a DecimalField with a max_digits of 10 and a decimal_places of 2.

Contributions are also related to the Entity model below to track which entity the contribution
is associated with over time so we can track contributions to candidates and PACs.

'''
class Contribution(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"${self.amount} from {self.donor} on {self.date}"
    

'''
Entity model

The Entity model will have required fields entity_name, office, year, report_name, state, and classification.
The entity_name field will be the name of the entity, which could be a PAC or a campaign name. The office
field will be the office being sought or held. The year field will be the year of the election or report.
The report_name field will be the name or identifier for the report. The state field will be the state code,
e.g., MN. The classification field will be a choice field with two options: Left and Right.

'''

class Entity(models.Model):
    # Define the choices for the classification field
    LEFT = 'L'
    RIGHT = 'R'
    CLASSIFICATION_CHOICES = [
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    ]
    
    first_name = models.CharField(max_length=255, null=True, blank=True)  # Optional, for candidates
    last_name = models.CharField(max_length=255, null=True, blank=True)   # Optional, for candidates
    entity_name = models.CharField(max_length=255)  # Required, for PACs or campaign names
    is_candidate = models.BooleanField(default=False)  # Distinguish between candidates and PACs
    office = models.CharField(max_length=255)  # Office being sought or held
    year = models.IntegerField()  # Year of the election or report
    report_name = models.CharField(max_length=255)  # Name or identifier for the report
    state = models.CharField(max_length=2)  # State code, e.g., MN
    classification = models.CharField(
        max_length=1,
        choices=CLASSIFICATION_CHOICES,
        default=RIGHT,
    )

    def __str__(self):
        return f"{self.entity_name} ({self.year}) - {self.state}"