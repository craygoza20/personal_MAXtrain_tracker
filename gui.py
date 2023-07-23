from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import gtfs_realtime_requests as gtfs
import json
class ResultsScreen(Screen):
    pass

class SearchApp(App):
    def build(self):
        # Create a ScreenManager
        self.screen_manager = ScreenManager()

        # Create the landing screen
        self.landing_screen = Screen(name='landing')
        layout = BoxLayout(orientation='vertical')
        self.search_input = TextInput(hint_text='Search Line:', multiline=False)
        self.search_button = Button(text='Search', on_press=self.on_search)
        layout.add_widget(self.search_input)
        layout.add_widget(self.search_button)
        self.landing_screen.add_widget(layout)

        # Create the results screen
        self.results_screen = ResultsScreen(name='results')
        layout = BoxLayout(orientation='vertical')
        self.results_text = TextInput(readonly=True, multiline=True, halign='left', font_size=20, scroll_y=0)
        layout.add_widget(self.results_text)

        # Create the "Back" button
        back_button = Button(text='Back', on_press=self.go_to_landing_screen)
        layout.add_widget(back_button)

        self.results_screen.add_widget(layout)

        # Add the screens to the ScreenManager
        self.screen_manager.add_widget(self.landing_screen)
        self.screen_manager.add_widget(self.results_screen)

        return self.screen_manager

    def on_search(self, instance):
        # This function will be called when the button is pressed
        search_line = self.search_input.text
        # Perform the search or any action you want with the search_line
        # For this example, we'll just update the results_text with the search_line
        payload = gtfs.default_payload.copy()
        self.results_text.text = ""

        # Update the payload with the user-submitted parameter
        if search_line:
            # Assuming the user-submitted parameter is a JSON-formatted string
            try:
                user_param = json.loads(search_line)
                payload.update(user_param)
            except json.JSONDecodeError:
                # Handle the case where the user-submitted parameter is not a valid JSON
                self.results_text.text = "Error: Invalid JSON parameter. Please try again."
                return
                

        # Now, 'payload' contains the default payload with the user-submitted parameter (if provided)
        # Call the API function with 'payload' to get the arrival data
        try:
            arrival_data = gtfs.get_arrivals(payload)
            # formatted_json = json.dumps(arrival_data, indent=1)
            for arrival in arrival_data:
                for item in arrival.items():
                    self.results_text.text += str(item) +'\n'
                self.results_text.text += '\n--------------------\n'

        except Exception as e:
            # Handle API request errors here
            self.results_text.text = f"Error: {str(e)}"
        
        # Set scroll_y to 1 to make the text start from the top
        self.results_text.cursor = (0,0)
        # Switch to the results screen
        self.screen_manager.current = 'results'

        # Clear the search entry box
        self.search_input.text = ""


    def go_to_landing_screen(self, instance):
        # Function to go back to the landing screen
        self.screen_manager.current = 'landing'

if __name__ == '__main__':
    SearchApp().run()
