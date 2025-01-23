import nuke
import subprocess
import os

# Define the function as a global method
def run_script():
    try:
        features = []
        face_node = nuke.thisNode()
        if face_node["whole_face"].value():
            features.append("WHOLE_FACE")
        if face_node["nose"].value():
            features.append("NOSE")
        if face_node["crows_feet_left"].value():
            features.append("CROWS_FEET_LEFT")
        if face_node["crows_feet_right"].value():
            features.append("CROWS_FEET_RIGHT")
        if face_node["eye_left"].value():
            features.append("EYE_LEFT")
        if face_node["eye_right"].value():
            features.append("EYE_RIGHT")
        if face_node["above_eye_left"].value():
            features.append("ABOVE_EYE_LEFT")
        if face_node["above_eye_right"].value():
            features.append("ABOVE_EYE_RIGHT")
        if face_node["under_eye_left"].value():
            features.append("UNDER_EYE_LEFT")
        if face_node["under_eye_right"].value():
            features.append("UNDER_EYE_RIGHT")
        if face_node["mouth_inside"].value():
            features.append("MOUTH_INSIDE")
        if face_node["lip_upper"].value():
            features.append("LIP_UPPER")
        if face_node["lip_lower"].value():
            features.append("LIP_LOWER")
        if face_node["left_of_nose"].value():
            features.append("LEFT_OF_NOSE")
        if face_node["right_of_nose"].value():
            features.append("RIGHT_OF_NOSE")
        if face_node["nose_bridge"].value():
            features.append("NOSE_BRIDGE")

        input_dir = "J:/Portfolio_2024/NukePratice/Deage/OpenCV/test_image_seq"
        output_dir = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(nuke.root().knob('name').value())), "masks"))
        print("FEATURES TO INCLUDE:")
        print(features)

        features = ",".join(map(str, features))

        # Mediapipe script path
        mediapipe_script = "C:/Users/Keith/PycharmProjects/pythonProject/NukeScripts/generate_face_masks.py"
        python_executable = "C:/Users/Keith/AppData/Local/Programs/Python/Python310/python.exe"


        # Build the command
        command = [python_executable,
                   mediapipe_script,
                   "--input_dir", input_dir,
                   "--output_dir", output_dir,
                   "--features", features]
        print("COMMAND:")
        print(command)
        result = subprocess.run(command, check=True)

        # Load mask sequence
        mask_filepath = os.path.normpath(os.path.join(output_dir, "{}_mask_####.jpg".format(features.replace(",","-"))))
        mask_filepath = mask_filepath.replace("\\", "/")
        with nuke.root():
            mask = nuke.nodes.Read(file=mask_filepath)
            mask["first"].setValue(int(nuke.Root()['first_frame'].value()))
            mask["last"].setValue(int(nuke.Root()['last_frame'].value()))
            mask.setName("Masks{}".format(features))
        print("Generate Face Masks script executed successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

def create_face_mask_node():
    face_mask_node = nuke.createNode("Group")
    face_mask_node.setName("FaceMaskNode")

    # Add knobs
    face_mask_node.addKnob(nuke.Text_Knob("Create masks for:"))

    whole_face = nuke.Boolean_Knob("whole_face", "Whole Face")
    nose = nuke.Boolean_Knob("nose", "Nose")
    crows_feet_left = nuke.Boolean_Knob("crows_feet_left", "Crows Feet Left")
    crows_feet_right = nuke.Boolean_Knob("crows_feet_right", "Crows Feet Right")
    eye_left = nuke.Boolean_Knob("eye_left", "Eye Left")
    eye_right = nuke.Boolean_Knob("eye_right", "Eye Right")
    above_eye_left = nuke.Boolean_Knob("above_eye_left", "Above Eye Left")
    above_eye_right = nuke.Boolean_Knob("above_eye_right", "Above Eye Right")
    under_eye_left = nuke.Boolean_Knob("under_eye_left", "Under Eye Left")
    under_eye_right = nuke.Boolean_Knob("under_eye_right", "Under Eye Right")
    mouth_inside = nuke.Boolean_Knob("mouth_inside", "Mouth Inside")
    lip_upper = nuke.Boolean_Knob("lip_upper", "Lip Upper")
    lip_lower = nuke.Boolean_Knob("lip_lower", "Lip Lower")
    left_of_nose = nuke.Boolean_Knob("left_of_nose", "Left of Nose")
    right_of_nose = nuke.Boolean_Knob("right_of_nose", "Right of Nose")
    nose_bridge = nuke.Boolean_Knob("nose_bridge", "Nose Bridge")

    face_mask_node.addKnob(whole_face)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(nose)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(crows_feet_left)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(crows_feet_right)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(eye_left)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(eye_right)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(above_eye_left)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(above_eye_right)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(under_eye_left)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(under_eye_right)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(mouth_inside)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(lip_upper)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(lip_lower)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(left_of_nose)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(right_of_nose)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))
    face_mask_node.addKnob(nose_bridge)
    face_mask_node.addKnob(nuke.Text_Knob("", ""))

    face_mask_node.addKnob(nuke.PyScript_Knob("run_script", "Generate Face Masks"))

    # Assign the action to the PyScript button using a string
    face_mask_node['run_script'].setCommand("run_script()")

# Add the node to the custom menu
toolbar = nuke.toolbar("Nodes")
my_menu = toolbar.addMenu("Custom Tools")
my_menu.addCommand("Face Mask Node", create_face_mask_node)
