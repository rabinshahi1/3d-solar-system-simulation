import dearpygui.dearpygui as dpg

class UIPanel:
    def __init__(self, planets_details):
        self.planet_data = planets_details
        
        dpg.create_context()
        dpg.create_viewport(title="3D Solar System UI", width=400, height=400)
        
        with dpg.window(label="Planet Selector", width=400, height=400):
            self.planet_list = list(self.planet_data.keys())  # Get planet names from loaded data
            for planet in self.planet_list:
                # Create a callback for each button using a helper function
                callback = self.get_callback(planet)
                dpg.add_button(label=planet, callback=callback)
            
            self.planet_info = dpg.add_text("Select a planet to view details.")
        
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def get_callback(self, planet):
        """Return a callback function that captures the current planet."""
        def callback(sender, app_data):
            self.select_planet(planet)
        return callback

    def select_planet(self, planet):
        # Retrieve the details for the selected planet from the loaded data
        planet_info = self.planet_data.get(planet, {})
        description = planet_info.get("description", "No description available.")
        facts = "\n".join(planet_info.get("facts", ["No facts available."]))
        sattelite=planet_info.get("satellites", "No sattelite available.")
        
        # Display planet details in the UI
        dpg.set_value(self.planet_info, f"Selected: {planet}\nDescription: {description}\nFacts:\n{facts}\nSattelite: {sattelite}")
        
        # This line should now print the correct planet name
        print(f"Camera should move to: {planet}")

    def render(self):
        dpg.render_dearpygui_frame()

