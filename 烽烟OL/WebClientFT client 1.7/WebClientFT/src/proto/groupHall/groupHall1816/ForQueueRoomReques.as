package proto.groupHall.groupHall1816 {
	import com.netease.protobuf.*;
	import flash.utils.IExternalizable;
	import flash.utils.IDataOutput;
	import flash.utils.IDataInput;
	import flash.errors.IOError;
	// @@protoc_insertion_point(imports)
	// @@protoc_insertion_point(class_metadata)
	public final class ForQueueRoomReques extends Message implements IExternalizable {
		public var id:int;
		public var readyStatu:int;
		public function writeExternal(output:IDataOutput):void {
			WriteUtils.writeTag(output, WireType.VARINT, 1);
			WriteUtils.write_TYPE_INT32(output, id);
			WriteUtils.writeTag(output, WireType.VARINT, 2);
			WriteUtils.write_TYPE_INT32(output, readyStatu);
		}
		public function readExternal(input:IDataInput):void {
			var idCount:uint = 0;
			var readyStatuCount:uint = 0;
			while (input.bytesAvailable != 0) {
				var tag:Tag = ReadUtils.readTag(input);
				switch (tag.number) {
				case 1:
					if (idCount != 0) {
						throw new IOError('Bad data format.');
					}
					++idCount;
					id = ReadUtils.read_TYPE_INT32(input);
					break;
				case 2:
					if (readyStatuCount != 0) {
						throw new IOError('Bad data format.');
					}
					++readyStatuCount;
					readyStatu = ReadUtils.read_TYPE_INT32(input);
					break;
				default:
					ReadUtils.skip(input, tag.wireType);
				}
			}
			if (idCount != 1) {
				throw new IOError('Bad data format.');
			}
			if (readyStatuCount != 1) {
				throw new IOError('Bad data format.');
			}
		}
	}
}
