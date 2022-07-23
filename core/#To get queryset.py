#To get queryset

def get_queryset():
    queryset = {
        'allprojects': Project.objects.all(),
        'allcategories': Category.objects.all()
        }
    return queryset

