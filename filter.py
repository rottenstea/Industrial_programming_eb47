import xml.etree.ElementTree as ET

class XMLFilter:
    """
    A class to parse and filter XML data containing astronomical event information.
    The class handles coordinate data and various astronomical parameters.
    """
    
    def __init__(self, xml_content):
        """
        Initialize the XMLFilter with XML content.
        
        Args:
            xml_content (str): XML content as a string to be parsed
        """
        # Parse the XML content directly from string
        self.root = ET.fromstring(xml_content)
        #self.root = ET.parse(xml_content)

        # Initialize coordinate attributes
        self.ra = None  # Right Ascension
        self.dec = None  # Declination
        
        # Set the observable declination threshold
        self.observable_dec_threshold = 48.026 - 90  # Minimum observable declination
    
    def get_text(self, element_name):
        """
        Get text content from a specified XML element.
        
        Args:
            element_name (str): Name of the XML element to search for
            
        Returns:
            str: Text content of the element, or None if not found
        """
        for child in self.root.iter(element_name):
            return child.text
        return None
    
    def get_value(self, param_name):
        """
        Get value of a parameter from XML Param elements.
        
        Args:
            param_name (str): Name attribute of the Param element to search for
            
        Returns:
            str: Value attribute of the matching Param element, or None if not found
        """
        for child in self.root.iter('Param'):
            if child.get('name') == param_name:
                return child.get('value')
        return None

    def get_text(self, tag):
        """
        Get text of a parameter from XML Param elements.
        """
        for child in self.root.iter(tag):
            return(child.text)
        return None
    
    def is_observable(self):
        """
        Check if the event is observable based on its declination.
        
        Returns:
            bool: True if observable, False otherwise
        """
        dec = float(self.get_text('C2'))
        return dec >= self.observable_dec_threshold
    
    def get_location_status(self):
        """
        Get a human-readable status of the event's observability.
        
        Returns:
            str: Message indicating whether the event is observable
        """
        if self.is_observable():
            return 'The event should be observable.'
        return 'The event is below the observable Declination.'
    
    def get_event_data(self):
        """
        Collect and format all relevant event data.
        
        Returns:
            dict: Dictionary containing all event parameters and status
        """
        return {
            'coordinates': {
                'RA': self.get_text('C1'),
                'Dec': self.get_text('C2')
            },
            'observable': self.is_observable(),
            'parameters': {
                'Sun_Distance': self.get_value('Sun_Distance'),
                'Moon_Distance': self.get_value('MOON_Distance'),
                'Moon_Illumination': self.get_value('Moon_Illum'),
                'Date' : self.get_text('Date')
            }
        }
    
    def print_data(self):
        """
        Print a formatted report of the event data.
        Similar to the original Data() function but with improved formatting.
        """
        data = self.get_event_data()
        
        print('The coordinate values of the event are: ')
        print(f"RA: {data['coordinates']['RA']} deg, Dec: {data['coordinates']['Dec']} deg")
        print(self.get_location_status())
        print("")
        print('The parameters of the event are: ')
        print(f"Date of Observation: {data['parameters']['Date']}")
        print(f"Sun Distance: {data['parameters']['Sun_Distance']} deg")
        print(f"Moon Distance: {data['parameters']['Moon_Distance']} deg")
        print(f"Moon Illumination: {data['parameters']['Moon_Illumination']} %")