from django.urls import include, path
from .views import male, female, general

urlpatterns = [



    path("/question", female.AddQuestion, name='add_question'),
    path("/deletequestion/<int:question_pk>/", female.DeleteQuestion, name='delete_question'),
    path("/editquestion/<int:question_pk>/", female.EditQuestion, name='edit_question'),
    path('showquestions/<pk>', male.ShowQuestion, name='showquestion'),
    path('proposalquestion/<pk>', male.QuestionAnswer, name='female_question'),


    
    path('/myquestions/', female.AllQuestion, name='all_question'),
 
    path('male/', include(([

        path("male_dashboard", male.Dashboard, name='dashboard'),

        path("profile", male.MaleProfile.as_view(), name='male_profile'),
        path("updateprofile/<int:pk>/", male.EditMaleProfile.as_view(), name='edit_male_profile'),


        path("aboutme", male.MaleAboutMe.as_view(), name='male_aboutme'),
        path("updateaboutme/<int:pk>/", male.EditMaleAboutMe.as_view(), name='edit_male_aboutme'),



        path("religion", male.MaleReligion.as_view(), name='male_religion'),
        path("updatereligion/<int:pk>/", male.EditMaleReligion.as_view(), name='edit_male_religion'),


        path("male_character", male.MaleCharacter.as_view(), name='male_character'),
        path("updatecharacter/<int:pk>/", male.EditMaleCharacter.as_view(), name='edit_male_character'),



        path("male_family", male.MaleFamily.as_view(), name='male_family'),
        path("updatefamily/<int:pk>/", male.EditMaleFamily.as_view(), name='edit_male_family'),


        path("male_education", male.MaleEducation.as_view(), name='male_education'),
        path("updateeducation/<int:pk>/", male.EditMaleEducation.as_view(), name='edit_male_education'),



        path("male_contact", male.MaleContact.as_view(), name='male_contact'),
        path("updatecontact/<int:pk>/", male.EditMaleContact.as_view(), name='edit_male_contact'),




    

        
        
      
        
       
       

        




        


        path("details/<pk>/", male.FemaleDetails, name='female_details'),


       



        


        #path("interest/<pk>/", male.FemaleInterest, name='female_interest'),

        path("showinterest/<pk>/", male.MyInterest, name='female_showinterest'),

        

        path("exam_completed", male.ExamCompleted, name='exam_completed'),


        





        


        


        


        


        
        
            


    ], 'app'), namespace='male')),

    path('female/', include(([

        path("female_dashboard", female.Dashboard, name='dashboard'),


        path("female_profile", female.FemaleProfile.as_view(), name='female_profile'),
        path("edit_female_profile/<int:pk>/", female.EditFemaleProfile.as_view(), name='edit_female_profile'),
        
        
        
        path("female_family", female.FemaleFamily.as_view(), name='female_family'),
        path("edit_female_family/<int:pk>/", female.EditFemaleFamily.as_view(), name='edit_female_family'),





        path("female_education", female.FemaleEducation.as_view(), name='female_education'),
        path("edit_female_education/<int:pk>/", female.EditFemaleEducation.as_view(), name='edit_female_education'),



        path("female_contact", female.FemaleContact.as_view(), name='female_contact'),
        path("edit_female_contact/<int:pk>/", female.EditFemaleContact.as_view(), name='edit_female_contact'),





        


        path("female_aboutme", female.FemaleAboutMe.as_view(), name='female_aboutme'),
        path("edit_female_aboutme/<int:pk>/", female.EditFemaleAboutMe.as_view(), name='edit_female_aboutme'),

        


        path("female_religion", female.FemaleReligion.as_view(), name='female_religion'),
        path("edit_female_religion/<int:pk>/", female.EditFemaleReligion.as_view(), name='edit_female_religion'),

        path("female_character", female.FemaleCharacter.as_view(), name='female_character'),
        path("edit_female_character/<int:pk>/", female.EditFemaleCharacter.as_view(), name='edit_female_character'),

         


        
        

       


        


      
        #path('female/<int:pk>/', female.QuizUpdateView.as_view(), name='quiz_change'),
        #path('quiz/<int:course_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),


        path('myoffer', female.MyOffer, name='my_offer'),
        path('result/<pk>', female.Result, name='male_proposal'),


        path('all_proposal', female.MyAllProposal, name='allproposal'),

        path("details/<pk>/", female.MaleDetails, name='male_details'),

        path('acceptproposal/<pk>', female.AcceptMaleProposal, name='accept_proposal'),

        path('rejectproposal/<pk>', female.EjectMaleProposal, name='reject_proposal'),



        


        



    ], 'app'), namespace='female')),

]