import os
from PIL import Image

imgname = "r_abductor.png" # Fixed value for imgname, will later be called upon to read a whole file of race pngs. img stands for image
rname = "abductor" # Fixed value for rname, will later be called upon to read the png names.  r stands for race
xtopleft = 0 # initial X value for image cropping on the top left.
ytopleft = 0 # initial Y value for image cropping on the top left.
xbotright= 32# initial X value for image cropping on the bottom right.
ybotright= 32# initial Y value for image cropping on the bottom right.
#
xcoord = 0 # coordinate found for x on image
ycoord = 0 # coordinate found for y on image
xpaste = 0
xvalonsheet = 9
yvalonsheet = 8
rsnewpartslist =[["groin_f_s","groin_f_n","groin_f_e","groin_f_w","groin_m_s","groin_m_n","groin_m_e","groin_m_w","head_f_s"],
                 ["head_f_n","head_f_e","head_f_w","head_m_s","head_m_n","head_m_e","head_m_w","leftarm_s","leftarm_n"],
                 ["leftarm_e","leftarm_w","leftfoot_s","leftfoot_n","leftfoot_e","leftfoot_w","lefthand_s","lefthand_n","lefthand_e"],
                 ["lefthand_w","leftleg_s","leftleg_n","leftleg_e","leftleg_w","overlay_husk_s","overlay_husk_n","overlay_husk_e","overlay_husk_w"],
                 ["rightarm_s","rightarm_n","rightarm_e","rightarm_w","rightfoot_s","rightfoot_n","rightfoot_e","rightfoot_w","righthand_s"],
                 ["righthand_n","righthand_e","righthand_w","rightleg_s","rightleg_n","rightleg_e","rightleg_w","torso_f_s","torso_f_n"],
                 ["torso_f_e","torso_f_w","torso_f_fat_s","torso_f_fat_n","torso_f_fat_e","torso_f_fat_w","torso_m_s","torso_m_n","torso_m_e"],
                 ["torso_m_w","torso_m_fat_s","torso_m_fat_n","torso_m_fat_e","torso_m_fat_w","d1","d2","d3","d4"]]
# ^ unused variable rsnewpartslist, displays race part names in orientation from south, north, east, and west. (snew)


rpartslist = ["groin_f","groin_m","head_f","head_m","larm","lfoot","lhand","lleg","rarm","rfoot","rhand","rleg","chest_f","chest_fat_f","chest_m","chest_fat_m","overlay_husk","delete"]
# ^ displays race part names
rdirpieces = 4
rtotalparts = len(rpartslist)
rpage = Image.open(imgname)
print(rpage)
rtemp = rpage.crop((0,0,1,1))  # A literal single pixel saved (it really doesn't matter what it is, it will be overwritten)
rfull = rtemp.resize((128,32)) # Pixel is stretched into a 128x32 image for the 's-n-e-w' format
for v in range (rtotalparts):  #
    for b in range (rdirpieces):
        rpiece = rpage.crop((xtopleft, ytopleft, xbotright, ybotright))
        print (xtopleft, ytopleft, xbotright, ybotright) # de-bug check for all said variables here
        rfull.paste(rpiece,(xpaste,0))
        xbotright = xbotright + 32
        xtopleft = xtopleft + 32
        xpaste = (b+1) * 32
        if xbotright >= xvalonsheet*32+1:
            ybotright = ybotright + 32
            ytopleft = ytopleft + 32
            xbotright = 32
            xtopleft = 0
    xpaste = 0
    rfull.save("bodyparts_"+rname+"_"+rpartslist[v]+".png")
# bodyparts_vulpkanin_groin_f.png