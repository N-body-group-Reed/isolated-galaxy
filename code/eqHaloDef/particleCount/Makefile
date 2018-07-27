smallClassicL: 
	../../charmrun +p4 ++local ../../ChaNGa haloNFW.param
	../../charmrun +p4 ++local ../../ChaNGa haloJff.param
	../../charmrun +p4 ++local ../../ChaNGa haloHrn.param
	../../charmrun +p4 ++local ../../ChaNGa haloArb.param
bigClassic:
	../../charmrun +p100 ../../ChaNGa haloNFW.param
	../../charmrun +p100 ../../ChaNGa haloJff.param
	../../charmrun +p100 ../../ChaNGa haloHrn.param
	../../charmrun +p100 ../../ChaNGa haloArb.param
socket_test:
	../../charmrun ++oneWthPerSocket ++local ../../ChaNGa haloNFW.param
	../../charmrun ++oneWthPerSocket ++local ../../ChaNGa haloJff.param
	../../charmrun ++oneWthPerSocket ++local ../../ChaNGa haloHrn.param
	../../charmrun ++oneWthPerSocket ++local ../../ChaNGa haloArb.param
auto_test:
	../../charmrun ++auto-provision ++local ../../ChaNGa haloNFW.param
	../../charmrun ++auto-provision ++local ../../ChaNGa haloJff.param
	../../charmrun ++auto-provision ++local ../../ChaNGa haloHrn.param
	../../charmrun ++auto-provision ++local ../../ChaNGa haloArb.param
perpu_test:
	../../charmrun ++oneWthPerPU ++local ../../ChaNGa haloNFW.param
	../../charmrun ++oneWthPerPU ++local ../../ChaNGa haloJff.param
	../../charmrun ++oneWthPerPU ++local ../../ChaNGa haloHrn.param
	../../charmrun ++oneWthPerPU ++local ../../ChaNGa haloArb.param
clean:
	rm -rf *.log *.00* *.ppm
