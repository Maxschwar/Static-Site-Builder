
class HtmlNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This Method is not implemented here")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        result = ""
        for key, val in self.props.items():    
            result += f" {key}={val}"
        return result
    
    def __repr__(self):
        return f"""
        tag: {self.tag}
        value: {self.value}
        children: {self.children}
        props: {self.props}
    """
