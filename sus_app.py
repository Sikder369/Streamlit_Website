import streamlit as st
from PIL import Image

# 1. PAGE SETTINGS
# This controls browser title, icon, and page width.
# Memory trick:
# set_page_config = setting the website's ID card 🪪
# --------------------------------------------------

st.set_page_config(
    page_title="🧠 BrainWave by Susmita Sikder",
    page_icon="🧠",
    layout="wide"
)

# CUSTOM ORANGE + WHITE DESIGN
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #ffffff;
    }

    h1, h2, h3 {
        color: #e86f00;
    }

    .hero-box {
        background-color: #fff3e6;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #ff9f40;
        text-align: center;
        margin-bottom: 25px;
    }

    .post-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff7a00;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.12);
        margin-bottom: 15px;
    }

    .tagline {
        color: #444444;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# RESIZE IMAGE
# --------------------------------------------------

image = Image.open("n5.jpg")

image = image.resize((1400, 400))

st.image(image, use_container_width=True)

# HERO SECTION
# --------------------------------------------------

st.markdown(
    """
    <div class="hero-box">
        <h1>🧠 BrainWave by Susmita Sikder</h1>
        <p class="tagline">
            Unlocking the Secrets of the Brain, One Neuron at a Time
        </p>
        <p>
            Explore neuroscience, learning, memory, focus, and the amazing world inside your mind.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

home_tab, about_tab, courses_tab, posts_tab, contact_tab = st.tabs(
    ["🏠 Home", "👤 About", "📚 Topics", "📝 Posts", "📩 Contact"]
)

# --------------------------------------------------
# HOME TAB
# --------------------------------------------------

with home_tab:
    st.header("🏠 Welcome to BrainWave")


    st.markdown(
    """
    <div style='text-align: justify; font-size:24px; line-height:2;'>

    From India to Europe and Germany🚵🗺️ — a journey driven by curiosity, passion, and the dream of making neuroscience easy for everyone.  

    BrainWave by Sus Daa transforms complex brain science into simple, engaging, and beginner-friendly learning experiences 🚀. Here, science meets creativity 🎨, curiosity sparks discovery 🔍, and every lesson opens a new door into the fascinating world of the human brain 🧬✨.  

    From understanding memory and emotions to exploring neurons and cognition 💡, BrainWave creates a space where learning feels exciting, interactive, and inspiring 🌍📚.

    </div>
    """, unsafe_allow_html=True)


    st.success("Mission🔬: Make brain science easy enough for everyone to understand 🧠")



# ABOUT TAB
# --------->>>>--------------------->>-------------------->>>>>

with about_tab:
    st.header("👤 About BrainWave🐢👽")

   
    st.markdown("""
    <div style='text-align: justify; font-size:24px; line-height:2;'>

    🧠 Welcome to BrainWave by Sus Daa — a modern learning space created for curious minds who want to explore the amazing world of neuroscience 🌍✨. From memory, emotions, and focus 💭 to habits, learning, intelligence, and human behavior 🌟, this platform makes brain science simple, exciting, and easy to understand for everyone.  

    🚀 BrainWave transforms difficult neuroscience concepts into engaging and beginner-friendly lessons where science meets creativity 🎨 and curiosity leads to discovery 🔍. Every topic is designed to inspire imagination, encourage critical thinking, and make learning feel interactive and enjoyable 📚🧬.  

    💡 Whether you're a student, a future scientist, or simply fascinated by how the human mind works, BrainWave is your place to learn, explore, and grow through knowledge, curiosity, and discovery 🌈✨.

    </div>
    """, unsafe_allow_html=True
    )


# TOPICS TAB
# --------------------------------------------------

with courses_tab:
    st.header("📚 Learning Topics📑")

    st.markdown("""
<div style='font-size:22px; line-height:2;'>

<h3 style='color:#FF9933;'>
🌟 What You’ll Explore in BrainWave 🧠
</h3>

BrainWave brings together neuroscience, learning, and technology in a simple and exciting way 🚀✨.  
Here you will discover educational content about:

- 🧠 Neuroscience Basics & Brain Functions  
- 📝 Smart Study Skills & Learning Techniques  
- 🎯 Focus, Motivation & Productivity  
- 😴 Sleep, Memory & Brain Performance  
- 👩‍💻 MATLAB for Beginners  
- 💻 Basic Python Programming  
- 🌍 Human Behavior, Habits & Cognitive Science  
- 🔍 Interactive Learning & Creative Exploration  

📚 Designed to make complex topics simple, engaging, and beginner-friendly for curious minds everywhere ✨.

</div>
""", unsafe_allow_html=True)
    
# POSTS TAB
# --------------------------------------------------

with posts_tab:
    st.header("📝 Educational Posts")

    posts = [
        {
            "title": "How the Brain Learns",
            "date": "03, May 2026⏰",
            "content": """
            <div style='text-align: justify; font-size:18px; line-height:1.8;'>

            Every time you learn something new 📚✨, your brain creates and strengthens powerful connections between billions of neurons 🧬⚡. Through practice, repetition, curiosity, and understanding 🔍, these neural pathways become stronger and faster 🚀.  

            This amazing ability of the brain to grow and adapt is called neuroplasticity 🧠💡, helping improve memory, focus, creativity, and learning over time 🌟.

            </div>
            """
        },

        {
        "title": "📝 Best Memory Trick for Students",
        "date": "03, April 2026⏱️",
        "content": """
        <div style='text-align: justify; font-size:18px; line-height:1.8;'>

        Our brains remember information better when learning feels visual, emotional, and meaningful 🧠✨. Instead of only reading repeatedly 📚, try turning difficult ideas into stories, colorful images 🎨, or funny mental pictures 😂.  

        Repetition and active recall 🔍 also help strengthen memory pathways in the brain ⚡, making it easier to remember information during exams, presentations, and daily learning 🚀🌟.

        </div>
        """
        },

        {
        "title": "😴 Why Sleep Helps Learning⏲️",
        "date": "21, March 2026",
        "content": """
        <div style='text-align: justify; font-size:18px; line-height:1.8;'>

        Sleep is one of the brain’s most powerful learning tools 🧠✨. While you rest 😴, your brain organizes, processes, and stores the information you learned during the day 📚⚡. This process strengthens memory, improves focus, and helps the brain make better connections between ideas 🔍💡.  

        Studies show that good sleep can improve creativity 🎨, problem-solving 🚀, emotional balance 😊, and overall brain performance 🌟. In simple words — learning becomes stronger when the brain gets enough rest 🛌🧬.

        </div>
        """
        }
        ]

    for post in posts:
        st.markdown(
            f"""
            <div class="post-card">
                <h3>{post["title"]}</h3>
                <p><b>Date:</b> {post["date"]}</p>
                <p>{post["content"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.info("Later you can add more posts by adding new items inside the posts list.")

# CONTACT TAB
# --------------------------------------------------

with contact_tab:
    st.header("📩 Contact")

    st.write(
        """
        - Email: sikder004@gmail.com
        - Facebook: www.facebook.com/eurotravel9
        """ 
    )

    st.success("Visitors can contact you from this section.")


#-------======End For Now=====--------#