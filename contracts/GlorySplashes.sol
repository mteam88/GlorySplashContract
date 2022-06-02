
pragma solidity ^0.8.14;

import '@openzeppelin/contracts/token/ERC1155/ERC1155.sol';

contract GlorySplashes is ERC1155 {
    uint256 public constant MAXID=14;

    constructor() public ERC1155("ipfs://QmWQYDLsNQh7PuT4bNUvYHgSoF3bbQMUALDhQcvGViy968/{id}.json") {
        for (uint256 i=0; i<15; i++) {
        _mint(msg.sender, i, 1, "");
        }
    }
}