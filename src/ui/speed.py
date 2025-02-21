import dearpygui.dearpygui as dpg
class RotationPanel:
    def __init__(self):
       self.ospeed=1.0
       self.rspeed=1.0
       dpg.create_context()
       dpg.create_viewport(title="Dear PyGui Slider Example", width=300, height=100)

       with dpg.window(label="Basic Slider", width=300, height=100):
        
            dpg.add_slider_float(label="R-Speed", default_value=1.0, min_value=0.0, max_value=10.0, callback=self.slider_callback_one)
            dpg.add_slider_float(label="O-Speed", default_value=1.0, min_value=0.0, max_value=10.0, callback=self.slider_callback_two)

            
       dpg.setup_dearpygui()
       dpg.show_viewport()
        
    def slider_callback_one(self,sender, app_data):
        # print(f"Slider Value: {app_data}")
        self.rspeed=app_data
    def slider_callback_two(self,sender, app_data):
        # print(f"Slider Value: {app_data}")
        self.ospeed=app_data
        
        # return app_data
    def get_ospeed(self):
        return self.ospeed
    def get_rspeed(self):
        return self.rspeed

    # 
    # 
    def render(self):
        dpg.render_dearpygui_frame()