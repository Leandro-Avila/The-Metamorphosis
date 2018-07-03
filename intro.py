import pyglet

window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load('imagens/intro.mp4')

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)

pyglet.app.run()