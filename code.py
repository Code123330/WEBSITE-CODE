from PIL import Image
import requests
import streamlit as st
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


st.set_page_config(page_title="CodeBreaker Webpage", page_icon="tada:", layout="wide")



#--LOAD ASSETS--
imgx_form=Image.open("F:\WEBSITE-CODE\Images\Madara.jpg")
imgf_form=Image.open("F:\WEBSITE-CODE\Images\Bleach.jpg")
img_form=Image.open("F:\WEBSITE-CODE\Images\FB_IMG_16434493788513508.jpg")
imgw_form=Image.open("F:\WEBSITE-CODE\Images\FB_IMG_16434070358684565.jpg")
imgh_form=Image.open("F:\WEBSITE-CODE\Images\classroom.jpg")
imagk_form=Image.open("F:\WEBSITE-CODE\Images\My teen.jpg")

#--HEADEER SECTION--
with st.container():
    st.subheader("Hi, I am Code Breaker :wave:")
    st.title("Anime Inspirational Quotes")
    st.write("This site consist of anime inspirational quote")
    
#--QUOTES SECTION--
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Anime Quotes")
        st.write("##")
        st.write(
            """"
            
           Naruto Shippuden 

    Wake up to Reality! 

Nothing ever goes on as planned in this accursed world. 

The longer you live the more you will realize, 

that the only things that truly exist in this reality 

are merely pain, suffering and futility. 

  

Listen... 

Everywhere you look in this world 

wherever there is light, there will always be shadows to be found as well 

As long as there is the concept of victors, the vanquished will also exist. 

 

The self-intent of wanting to preserve peace, initiates wars. 

And hatred is born in order to protect love. 

 

There are nexuses and causal relationships that cannot be separated... 

I want to server the fate of this world... 

A world of only victors... 

A world of only peace... 

A world of only love... 

I will create such world 

             ... 

For truly this reality... 

Is a hell 
      ...
      
      Attack on Titan 
If you begin to regret, you’ll dull your future decisions and let others make your choices for you. All that’s left for you then is to die. Nobody can foretell the outcome. 
Each decision you make holds meaning only by affecting your next decision...  
      
            """
        )

with right_column:
    st.image(imgx_form)
    
with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.write("##")   
        st.write(
            """
            Cowboy Bebop  

Everything has a beginning and an end. 
Life is just a cycle of starts and stops.
There are ends we don’t desire, but they’re inevitable, 
we have to face them. It’s what being human is all about. 
...

One Piece 

You need to accept the fact that you’re not the best
and have all the will to strive to be better than anyone you face. 

            """
        )

with right_column:
    st.image(imgw_form)

#--IMAGE AND TEXT SECTION--
with st.container():
    st.write("---")
    image_column, text_column =st.columns((1, 2))
    with image_column:
        st.image(img_form)
    with text_column:
        st.subheader("Shakugan No Shana")
        st.write(
            """
Love is like a mirror that reflects your bad side. Especially when it’s unrequited, you get envious, jealous, prejudiced, and resentful.
You have to face all sorts of emotions, but there’s no reason to find that shameful.


                           Bleach
Humans die. Animals die. Plants die. 
Even soul reapers die. It’s the arch of the universe. 
Everything that comes to life eventually ceases to exist. 
                ...
                
             
             Rurouni Kenshin 
  Whatever you lose, you’ll find it again.
  But what you throw away, you’ll never get back.....
             
             
             
             Durarara!!
The only way to truly escape the mundane is for you to constantly be evolving. 
Whether you choose to aim high, or aim low.
Enjoy each day for what it is. 



                       One Piece 
Destiny. Fate. Dreams. These unstoppable ideas are held deep in the heart of man. 
As long as there are people who seek freedom in this life, these things shall not vanish from the Earth...
– 
            """
        )

with st.container():
    image_column, text_column=st.columns(2)
    with text_column:
        st.subheader("Bleach")
        st.write(
            """
             The perfect being you said?

Well, I have to tell you the honest truth as I see it .



It may well be a cliché after all,

but its the way things are.

That's precisely why ordinary men pursue the concept of perfection 

             Its infatuation

…
And the answer I came up with was. . .

Nothing!
Not one thing.


The truth of the matter is I despise perfection 


if something is perfect, that's it.

The bottom line becomes, there is no room for imagination.

No space for intelligence or ability or improvement.

Do you understand? 


To men of science like us, perfection is a dead end,

a condition of hopelessness.

Always strive to be better than anything that came before you but not perfect!


Scientists agonize over the attempt to achieve perfection

The kind of creatures we are. . . 

We take joy in trying to exceed our grasp . . . 

In trying to reach for something that in the end we have to admit...

In fact  be unreachable
     
In other words. . . .

You may think we operate on the same level but you're wrong

The moment you started talking about perfection you embraced an impossible concept 

And had already lost to me.. 

That is of course if you're indeed a scientist at all . . . .
            """
        )
    with image_column:
        st.image(imgf_form)
        
with st.container():
    st.write("---")
    st.subheader("Classroom OF The Elite")
    st.write("##")
    image_column, text_column=st.columns((1, 2))
    with image_column:
        st.image(imgh_form)
    with text_column:
        st.write(
            """ 
            
            
            
            
            
            
            
            
            If I may. . . 
            
I'd like to pose an interesting question. . . 

Are all human beings truly equal?
           . . .
These days everywhere you go there's a talk about the fight for equality

As a wise man once said...
"Heaven does not create one person above or below another. . . "


People like to throw his words around...
But that's not the whole quote

He goes on to say...

"While we are all equal at birth, pretty soon things begin to change"
  . . .
  
Academic effort is what set some people apart to rise above others

At any rate...


Humans change over time based on their actions . . .

Truth be told at the end of the day...

Equality is just a fantasy...

And most of us go through life denying the fact that we live in a meritocracy.
...






            """
        )
        
with st.container():
    st.subheader("My Teen Romantic comedy SNAFU")
    st.write("##")
    st.write("---")
    text_column, image_column=st.columns(2)
    with text_column:
        st.write(
            """
            Youth is a lie
            
Is Nothing but Evil

Those who rejoice in their youth...

Deceive themselves and those around them.

        .. . . . .
        
Accepting the circumstances that devour them...

In the fact of the great reverend Youth,

They will twist any common interpretation or accepted notion...

For recognition.  

        . . . 
        
In their minds, lies, secrets, sins and even failure are nothing...

More than the spice of youth...

    .. ..
If failure is truly the designated mark of one's Youth,

Then would it not be considered Abnormal for one..,

Not in this youth still fail at befriending anyone?

Buh I'm sure none of them would admit that being true.

                   . . . 
                   
They only define Youth to their own benefit...

In conclusion, I leave you with this. . . .

All you fools who delight in Youth...

       Drop dead.
             """
        )
    with image_column:
        st.image(imagk_form)
        
#--CONTACT----
with st.container():
    st.write("---")
    st.header("Get in touch with Me!")
    st.write("##")
    #Documentation
    contact_form = """
    <form action="https://formsubmit.co/sarfoisaac072@gamil.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
#LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by ",
        link("https://web.facebook.com/share/p/tuCkteUKAz2M5TP5/", "@sarfoisaac072"),
        br(),
        link("https://buymeacoffee.com/Code Breaker", image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
    




