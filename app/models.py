from django.db import models
from user.models import *
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField



def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

# Create your models here.

class Profile(models.Model):

    COMPLEX =  (
        ('Light','Light'),
        ('Dark','Dark'),
    )

    MARRIED =  (
        ('Divorced','Divorced'),
        ('Married','Married'),
        ('Never Married', 'Never Married'),
        ('Widowed', 'Widowed')
    )

    HEIGHT =  (
        ('4cm - 5cm','4cm - 5cm'),
        ('5cm - 6cm','6cm - 7cm'),
        
    )

    BODY =  (
        ('Athlete','Athlete'),
        ('Average','Average'),
        ('Heavy','Heavy'),
        ('Slim','Slim'),
        
    )


    PYHSICAL =  (
        
        ('Challenged','Challenged'),
        ('Normal','Normal'),
             
    )


    
    TRIBE =  (
        
        ('Yourba','Yoruba'),
        ('Hausa','Hausa'),
             
    )


    LANGUAGE =  (
        
        ('Yourba','Yoruba'),
        ('Hausa','Hausa'),
             
    )

    GROUP =  (
        
        ('A','A'),
        ('B', 'B'),
        ('AB','AB'),
        ('O', 'O')
             
    )

    

    GENOTYPE =  (
        
        ('AA','AA'),
        ('AS','AS'),
        ('SS','SS'),
             
    )



    
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    dob = models.DateField("Date of Birth")
    tribe = models.CharField("Tribe", max_length=500, choices=TRIBE)
    language = models.CharField("Language Spoken", max_length=150, choices=LANGUAGE)
    place_of_birth = models.CharField("Place of Birth", max_length=150)
    body_complex =  models.CharField("Complexion", max_length=50, choices=COMPLEX)
    marital = models.CharField("Martial Status", max_length=150, choices=MARRIED)
    height = models.CharField("Height", max_length=50, choices=HEIGHT)
    body = models.CharField("Body Type", max_length=50, choices=BODY)
    physical = models.CharField("Physical Challenges", max_length=150, choices=PYHSICAL)
    mention_challenges = models.CharField("If, Yes, Mention the form of Disability", max_length=250, null=True, blank=True)
    blood_group = models.CharField("Blood Group", max_length=10, choices=GROUP)
    blood_genotype = models.CharField("Blood Genotype", max_length=10, choices=GENOTYPE)
    image = models.FileField('Passport Photography', upload_to='passport', unique=True, validators=[validate_image], help_text='Maximum file size allowed is 2Mb')
    available = models.BooleanField("Availability", default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Family(models.Model):

    WELL =(
        ("First Class", "First Class"),
        ("Middle Class", "Middle Class"),
        ("Impoverished", "Impoverished")
    )

    user = models.OneToOneField(User, related_name="family", on_delete=models.CASCADE)
    father_name = models.CharField("Father's Name", max_length=50)
    father_job = models.CharField("What did your Father Do for Living", max_length=150)
    mother = models.CharField("Mother's Name", max_length=50)
    mother_job = models.CharField("What did your Mother Do for Living", max_length=150)
    well = models.CharField("Were your Parents well off",  max_length=150, choices=WELL)
    sibling = models.BooleanField("Do Your Have Siblings", default=True)
    sister = models.PositiveIntegerField("Number's of Sisters")
    brother = models.PositiveIntegerField("Number's of Brothers")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        
        verbose_name = 'Family'
        verbose_name_plural = 'Familys'



 

 
class Education(models.Model):
    
    JOB =  (
        
        ('Web Development','Web Development'),
        ('Software Development','Software Development'),
             
    )

    EDUCATION =  (
        
        ('PhD','PhD'),
        ('MSc.','MSc'),
        ('BSc.','BSc'),
        ('HND','HND'),
        ('OND','OND'),
        ('Undergraduate','Undergraduate'),
        ('Secondary School Leaving','Secondary School Leaving'),
        ('Primary School','Primary School'),
        ('non Aplicable','Non Applicable'),
             
    )
    

    user = models.OneToOneField(User, related_name="education", on_delete=models.CASCADE)
    job = models.CharField("Job Type", max_length=250, choices=JOB)
    job_description = models.CharField("Job Description", max_length=500)
    income = models.PositiveIntegerField("Yearly Income")
    education = models.CharField("Highest Level Education", max_length=250, choices=EDUCATION)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Eductaion'
        verbose_name_plural = 'Eductaions'


class Contact(models.Model):

    STATUS =  (
        
        ('Citizen','Citizen'),
        ('Visitation','Visitation'),
        ('Student','Student'),
             
    )

    user = models.OneToOneField(User, related_name="contact", on_delete=models.CASCADE)
    country = CountryField()
    status = models.CharField("Citizen Status", max_length=150, choices=STATUS)
    state = models.CharField("State", max_length=50)
    city = models.CharField("City", max_length=50)
    address = models.CharField("Personal Address", max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class AboutMe(models.Model):

    AVA =  (
        
        ('Currently available for Nikkah','Currently available for Nikkah'),
        ('Currently not available for Nikkah','Currently not available for Nikkah'),
             
    )

   

    user = models.OneToOneField(User, related_name="aboutme", on_delete=models.CASCADE)
    about_me = models.TextField("About Me")
    about_partner = models.TextField("About My Partner")
    availablity = models.CharField("Availability Status", max_length=500, choices=AVA)
    vision = models.CharField("My Vision", max_length=150)
    inspire = models.CharField("What inspires you must", max_length=150)
    favorite = models.CharField("What are your favorite things about yourself?", max_length=50)    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutMes'


class Religion(models.Model):


    RELIGIOUS =  (
        
        ('Muslim Since Birth','Muslim Since Birth'),
        ('Revert Muslim','Revert Muslim'),
             
    )


   

    SECT =  (
        
        ('Al-Sunnah','Al-Sunnah'),
        ('Salafi','Salafi'),
        ('Sufi', 'Sufi')
             
    )

    HIJAB =  (
        
        ("I am Male","I am Male"),
        ("I don't use Hijab","I dont use Hijab"),
        ('Scarf','Scarf'),
        ('Small-Hijab','Small-Hijab'),
        ('Mid-Hijab','Mid-Hijab'),
        ('Big-Hijab','Big-Hijab'),
        ('Khimar','Khimar'),
        ('Niqqab','Niqqab'),
             
    )


    BEARDS =  (
        
        ('I am Female','I am female'),
        ('I keep beards','I keep beards'),
        ('I dont keep it','I dont keep it'),
        ('I dont Have beards','I Dont have Beards'),
        ('Little','Little'),
       
             
    )

    user = models.OneToOneField(User, related_name="religion", on_delete=models.CASCADE)
    beards = models.CharField("Do You Keep Beards",  max_length=150, choices=BEARDS)
    hijab = models.CharField("Your Hijab", max_length=150, choices=HIJAB)
    religious = models.CharField("Religion History", max_length=250, choices=RELIGIOUS)
    program = models.CharField("Which Program Do you Attend", max_length=150)
    sect = models.CharField("Which Sect Do you Belong to", max_length=150, choices=SECT)
    imam = models.CharField("The Name of Imam where you Pray", max_length=150)
    imam_phone_number = models.CharField("Your Imam Phone Number", max_length=15, help_text="+23410938846")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'


class Character(models.Model):

    VERT =  (
        
        ('Introvert','Introvert'),
        ('Extrovert','Extrovert'),
             
    )

    user = models.OneToOneField(User, related_name='character', on_delete=models.CASCADE)
    childhood = models.CharField(" What was your childhood ambition?", max_length=150)
    sight = models.CharField("Do you believe in love at first sight?", max_length=150)
    love = models.CharField("Have you ever been in love?", max_length=150)
    display = models.CharField("How do you display love", max_length=150)
    phobia = models.CharField("What are your phobias in relationships?", max_length=150)
    verted = models.CharField("Are you introverted or extroverted?", max_length=50, choices=VERT) 
      

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'


'''
56. How do you deal with stress? 
57. If you use drugs or alcohol, how do you feel about it? Do you brag about it? Try to hide it? Try to give it up and fail? Have no problem with it?
58. What do you do to entertain yourself? 
59. What is your idea of a really fun time? 
60. What do you consider to be your most admirable personal quality?
61. What is your greatest personal failing, in your view?
62. Do you think others see it that way, or would they say something different about your strengths and weaknesses?
63. How do you handle conflict with someone else? Do you avoid fights, or are you aggressive? Or are you passive aggressive and only give the appearance of cooperation?
64. What are your politics? Are you conservative, liberal, or something else? Do you have no interest in politics?
86. Where are you in your life right now? What are you most pleased with right now?
87. What keeps you awake at night?
88. What is the most pressing problem you have at the moment?
89. Is there something that you need or want that you don’t have? For yourself or for someone important to you?
90. Why don’t you have it? What is in the way?
91. What do you have to do in order to get the thing you need?
92. What is stopping you from taking this step?
93. Is there something else that must happen first in order for you to take this step?
94. Is there someone else who needs or wants the same thing?
95. Can they help you get it?
96. Are they one of the things in the way?
97. What happens if you don’t get it? What do you stand to lose?
98. How will your life change if you do get this thing or solve this problem?
99. Will someone else suffer if you succeed?

'''

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return f'{self.user} - {self.text}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class TakenQuiz(models.Model):
    taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taker')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    selected_choice = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField('Was this attempt correct?', default=False, null=False)
    date = models.DateTimeField(auto_now_add=True)



class TakenQuestion(models.Model):
    taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='takerquestion')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questionstaker')
    answer = models.TextField("Answer")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.taker} - {self.question.user}'


    


class InterestData(models.Model):
    
    APPLICATION_CHOICES = (

        ('I', 'INTEREST'),
        ('L', 'LET US TALK'),
        ('S', 'LET US SEE'),
        {'F', 'FINAL STAGE'},
        {'R', 'REJECT OFFER'},
    )

    interester = models.ForeignKey(User, related_name='interester', on_delete=models.CASCADE)
    interestin = models.ForeignKey(User, related_name='interestin', on_delete=models.CASCADE)
    note = models.TextField("Interest Note", blank=True, null=True)
    acceptance = models.TextField("Proceed Note", blank=True, null=True)
    status = models.CharField(max_length=13, choices=APPLICATION_CHOICES, default='I')
    read = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f'{self.interester.username} - {self.interestin.username} - {self.get_status_display()}'

    class Meta:
       
        verbose_name = 'InterestData'
        verbose_name_plural = 'InterestDatas'

    def clean(self):
        if self.acceptance:
            self.acceptance = self.acceptance.strip()
