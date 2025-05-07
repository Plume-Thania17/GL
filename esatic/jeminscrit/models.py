from django.db import models
from django.core.validators import FileExtensionValidator

class Candidat(models.Model):
    CONCOURS_CHOICES = [
        ('L1', 'Licence 1'),
        ('L2', 'Licence 2'),
        ('L3', 'Licence 3'),
        ('M1', 'Master 1'),
        ('M2', 'Master 2'),
    ]
    
    NIVEAU_CHOICES = [
        ('Bac', 'Baccalauréat'),
        ('Bac+1', 'Bac +1'),
        ('Bac+2', 'Bac +2'),
        ('Bac+3', 'Bac +3'),
        ('Bac+4', 'Bac +4'),
    ]
    
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenoms = models.CharField(max_length=200, verbose_name="Prénoms")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    niveau_etudes = models.CharField(max_length=10, choices=NIVEAU_CHOICES, verbose_name="Niveau d'études")
    etablissement_origine = models.CharField(max_length=200, verbose_name="Établissement d'origine")
    concours_souhaite = models.CharField(max_length=2, choices=CONCOURS_CHOICES, verbose_name="Concours souhaité")
    email = models.EmailField(verbose_name="Adresse email")
    telephone = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    date_inscription = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    
    # Fichiers
    extrait_naissance = models.FileField(
        upload_to='extraits/',
        validators=[FileExtensionValidator(['pdf'])],
        verbose_name="Extrait de naissance (PDF)"
    )
    certificat = models.FileField(
        upload_to='certificats/',
        validators=[FileExtensionValidator(['pdf'])],
        verbose_name="Certificat de scolarité ou diplôme (PDF)"
    )
    lettre_motivation = models.FileField(
        upload_to='lettres/',
        validators=[FileExtensionValidator(['pdf'])],
        verbose_name="Lettre de motivation (PDF)"
    )
    diplome = models.FileField(
        upload_to='diplomes/',
        validators=[FileExtensionValidator(['pdf'])],
        verbose_name="Diplôme (PDF)"
    )
    photo = models.ImageField(
        upload_to='photos/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        verbose_name="Photo d'identité (JPG/PNG)"
    )
    
    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.get_concours_souhaite_display()}"
    
    class Meta:
        verbose_name = "Candidat"
        verbose_name_plural = "Candidats"