import star_halo as star

sim = star.StarHalo(n_particles=1e5, fname = "starHalo.out")
sim.make_halo()
sim.finalize()