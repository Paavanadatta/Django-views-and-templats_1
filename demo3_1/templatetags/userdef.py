from django import template

register=template.Library()

def lastupper(value):
    res=value[-1]
    return res

register.filter('lu',lastupper)
 
@register.filter(name="wish")
def getname(value):
    res=f"Hello Mr. {value} "
    return res
