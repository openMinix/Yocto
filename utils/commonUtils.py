import yocto

def render_template( template, **kwargs):
    """Renders the template with the given parameters """
    
    page_template = yocto.jinja_env.get_template( template )
    rendered_page = page_template.render ( **kwargs )
    
    return rendered_page
