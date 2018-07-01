import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
for delta in range(100):
    mc.setBlock(pos.x + delta, pos.y, pos.z, block.STONE.id)
    mc.setBlock(pos.x, pos.y + 2 * delta, pos.z, block.STONE.id)
    mc.setBlock(pos.x, pos.y, pos.z + 3 * delta, block.STONE.id)
