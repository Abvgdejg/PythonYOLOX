import av

c = av.open("/app/resources/develop_streem.ts")

for f in c.decode(video=0):
    f.to_image().save("test/frame_%d.jpg" % f.index)
