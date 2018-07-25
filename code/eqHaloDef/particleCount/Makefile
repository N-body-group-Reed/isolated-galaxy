smallClassicL: 
	../../charmrun +p4 ++local ../../ChaNGa eqHalo.param
bigClassic:
	../../charmrun +p100 ../../ChaNGa eqHalo.param
socket_test:
	../../charmrun ++oneWthPerSocket ++local ../../ChaNGa eqHalo.param
auto_test:
	../../charmrun ++auto-provision ++local ../../ChaNGa eqHalo.param
perpu_test:
	../../charmrun ++oneWthPerPU ++local ../../ChaNGa eqHalo.param
clean:
	rm -rf halo2.log
	rm -rf halo2.000*
	rm -rf *.ppm
