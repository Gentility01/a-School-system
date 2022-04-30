from student_management_app.models import Term, Classes

def terms(request):
    return{
        'terms':Term.objects.all()
    }
    
    
def classes(request):
    return{
        'c_class':Classes.objects.all()
    }
    
    
    